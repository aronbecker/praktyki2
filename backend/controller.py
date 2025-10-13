from flask import Blueprint
from models import Company
from flask import request, jsonify

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

