from flask import Blueprint
from models import Company, User
from flask import request, jsonify, abort
from authHandler import authenticate, AuthenticationResult

page = Blueprint('page', __name__)

@page.route('/companies')
def home():
    page = request.args.get("page")
    if page == None or not page.isdigit() or int(page) < 0:
        page = 0

    companies = Company.query.paginate(per_page=20, page=int(page)+1).items

    return jsonify(
        [company.to_dict() for company in companies]
    ) 

@page.route('/company/<int:company_id>')
def get_company(company_id):
    company = Company.query.get(company_id)

    if company is None:
        return jsonify({"error": "Company not found"}), 404

    return jsonify(company.to_dict())

@page.route('/me')
def me():
    auth: AuthenticationResult = authenticate(request)

    if not auth.isAuthenticated:
        return abort(403)

    userId = auth.session.user_id

    user: User = User.query.filter_by(id=userId).first()
    if not user:
        return abort(403)

    return jsonify({
        "email": user.email,
        "firstname": user.firstname,
        "lastname": user.lastname,
    })
