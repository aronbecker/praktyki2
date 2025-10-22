from flask import Blueprint
from utils import calculateCompanyRating
from models import Company, User, Opinion
from flask import request, jsonify, abort
from authHandler import authenticate, AuthenticationResult
from models.extensions import db

page = Blueprint('page', __name__)


@page.route('/companies')
def home():
    page = request.args.get("page", default=0, type=int)
    if page < 0:
        page = 0

    rating = request.args.get("rating", type=int)
    query = Company.query

    if rating is not None and 1 <= rating <= 5:
        query = query.filter(Company.rating >= rating)

    page_obj = query.paginate(per_page=20, page=page + 1)
    companies = page_obj.items

    return jsonify({
        'pages': page_obj.pages,
        'companies': [company.to_dict() for company in companies]
    })



@page.route('/company/<int:company_id>')
def get_company(company_id):
    company = Company.query.get(company_id)

    if company is None:
        return jsonify({"error": "Nie znaleźiono firmy"}), 404

    return jsonify(company.to_dict())


@page.route('/me')
def me():
    auth: AuthenticationResult = authenticate(request)
    if not auth.isAuthenticated:
        return abort(403)

    user = auth.session.user

    return jsonify({
        "email": user.email,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "role": user.role
    })


@page.route('/company/<int:company_id>/comments', methods=['POST'])
def add_opinion(company_id):
    auth: AuthenticationResult = authenticate(request)
    if not auth.isAuthenticated:
        return abort(403)

    user = auth.session.user

    company = Company.query.get(company_id)
    if not company:
        return jsonify({"error": "Nie znaleziono firmy o podanym ID."}), 404

    existing_opinion = Opinion.query.filter_by(user_id=auth.session.user_id).filter(Opinion.company.has(id=company_id)).first()
    if existing_opinion:
        return jsonify({"error": "Dodałeś już opinię o tej firmie."}), 409

    data = request.get_json()
    rating = data.get('rating')
    comment = data.get('comment')

    if not rating or not isinstance(rating, (int, float)) or rating < 1 or rating > 5:
        return jsonify({"error": "Ocena musi być liczbą z zakresu od 1 do 5."}), 400

    if not comment or len(comment.strip()) == 0:
        return jsonify({"error": "Komentarz nie może być pusty."}), 400

    new_opinion = Opinion(
        user=user,
        company=company,
        rating=rating,
        comment=comment.strip()
    )

    db.session.add(new_opinion)
    db.session.commit()

    calculateCompanyRating(company_id)

    return "", 200


@page.route('/company/<int:company_id>/comments', methods=['GET'])
def get_company_comments(company_id):
    company = Company.query.get(company_id)

    if company is None:
        return jsonify({"error": "Nie znaleźiono firmy"}), 404

    return jsonify({
        "comments": [
            o.toStr() for o in company.opinions
        ]
    })

