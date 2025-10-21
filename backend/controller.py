from flask import Blueprint
from models import Company, User, Opinion
from flask import request, jsonify, abort
from authHandler import authenticate, AuthenticationResult
from app import db


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
        "role": user.role
    })


@page.route('/company/<int:company_id>/opinion', methods=['POST'])
def add_opinion(company_id):
    auth: AuthenticationResult = authenticate(request)

    if not auth.isAuthenticated:
        return abort(403)

    user_id = auth.session.user_id
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return abort(403)

    company = Company.query.get(company_id)
    if not company:
        return jsonify({"error": "Nie znaleziono firmy o podanym ID."}), 404

    existing_opinion = Opinion.query.filter_by(user_id=user_id, company_id=company_id).first()
    if existing_opinion:
        return jsonify({"error": "Dodałeś już opinię o tej firmie."}), 400

    data = request.get_json()
    rating = data.get('rating')
    comment = data.get('comment')

    if not rating or not isinstance(rating, (int, float)) or rating < 1 or rating > 5:
        return jsonify({"error": "Ocena musi być liczbą z zakresu od 1 do 5."}), 400

    if not comment or len(comment.strip()) == 0:
        return jsonify({"error": "Komentarz nie może być pusty."}), 400

    new_opinion = Opinion(
        user_id=user_id,
        company_id=company_id,
        rating=rating,
        comment=comment.strip()
    )

    db.session.add(new_opinion)
    db.session.commit()

    return "", 200


@page.route('/company/<int:company_id>/opinions', methods=['GET'])
def get_company_opinions(company_id):
    company = Company.query.get(company_id)
    if not company:
        return jsonify({"error": "Nie znaleziono firmy o podanym ID."}), 404

    page_param = request.args.get("page", default=0)

    if not str(page_param).isdigit() or int(page_param) < 0:
        page_param = 0
    else:
        page_param = int(page_param)

    opinions_page = Opinion.query.filter_by(company_id=company_id).order_by(Opinion.id.desc()).paginate(
        per_page=10, page=page_param + 1
    )

    opinions = opinions_page.items

    return jsonify({
        "liczba_stron": opinions_page.pages,
        "opinie": [
            {
                "id": o.id,
                "uzytkownik_id": o.user_id,
                "ocena": o.rating,
                "komentarz": o.comment,
                "data_dodania": o.created_at.isoformat() if o.created_at else None
            } for o in opinions
        ]
    })

