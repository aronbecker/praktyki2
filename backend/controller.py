from flask import Blueprint
from dtos.addOpinionDto import AddOpinionDto
from utils.requestToDtoConverter import convert
from models.category import Category
from utils import calculateCompanyRating
from models import Company, Opinion
from flask import request, jsonify, abort
from authHandler import authenticate, AuthenticationResult
from models.extensions import db
from datetime import datetime, timedelta, timezone

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

    # category = request.args.get("category", type=str)
    # if (category):
    #     query = query.filter(category in for c in Company.categories)

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
    reqData = convert(data, AddOpinionDto)

    if not reqData.rating or not isinstance(reqData.rating, (int, float)) or reqData.rating < 1 or reqData.rating > 5:
        return jsonify({"error": "Ocena musi być liczbą z zakresu od 1 do 5."}), 400

    if not reqData.comment:
        reqData.comment = ""

    new_opinion = Opinion(
        user=user,
        company=company,
        rating=reqData.rating,
        comment=reqData.comment.strip()
    )
    
    utc_plus_2 = timezone(timedelta(hours=2))
    new_opinion.creation_date = datetime.now(utc_plus_2)

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
            o.toStr() for o in company.opinions if o.comment != ""
        ]
    })

@page.route('/categories')
def getAllCategories():
    categories = [c.name for c in Category.query.all()]

    return jsonify({
        "categories" : categories
    }), 200