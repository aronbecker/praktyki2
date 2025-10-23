from flask import Blueprint
from dtos.companyDto import CompanyDto
from utils.requestToDtoConverter import convert
from models import Company, User, Address, Category, db
from flask import request, abort
from authHandler import authenticate, isAdmin

admin = Blueprint('admin', __name__)


@admin.route('/admin/addCompany', methods=['POST'])
def addCompany():
    user = throwIfNotAdmin(request)
    if (user == None): return
    
    data = request.get_json()

    company_ = convert(data, CompanyDto)

    town = data.get("town").strip()
    street = data.get("street").strip()
    building_number = data.get("building_number").strip()
    apartment_number = data.get("apartment_number")

    addres = Address(
        town,
        street,
        building_number,
        apartment_number
    )

    company = Company(
        company_.name,
        company_.phoneNumber,
        company_.email,
        company_.ownerName,
        company_.website,
        company_.nip,
        company_.regon
    )

    categoriesEntities = []

    for name in company_.categories:
        name = name.strip()
        category = Category.query.filter_by(name=name).first()
        if not category:
            category = Category(name=name)
        categoriesEntities.append(category)

    company.categories = categoriesEntities
    company.address = addres

    db.session.add(company)
    db.session.commit()

    return "", 200

@admin.route('/admin/company/<int:company_id>', methods=["PATCH"])
def editCompany(company_id):
    user = throwIfNotAdmin(request)
    if (user == None): return
    
    company = Company.query.filter_by(id=company_id).first_or_404()

    data = request.get_json()

    company.name = data.get('name').strip()
    company.owner_name = data.get('ownerName').strip()
    company.phone_number = data.get("phoneNumber").strip()
    company.email = data.get("email").strip()
    company.website_url = data.get("website").strip()
    company.nip = data.get("nip").strip()
    company.regon = data.get("regon").strip()

    company.address.town = data.get("town").strip()
    company.address.street = data.get("street").strip()
    company.address.building_number = data.get("building_number").strip()
    company.address.apartment_number = data.get("apartment_number")

    categories = data.get("categories")

    categoriesEntities = []

    for name in categories:
        name = name.strip()
        category = Category.query.filter_by(name=name).first()
        if not category:
            category = Category(name=name)
        categoriesEntities.append(category)

    company.categories = categoriesEntities

    db.session.commit()

    return "", 200


@admin.route('/admin/company/<int:company_id>', methods=['DELETE'])
def deleteCompany(company_id):
    user = throwIfNotAdmin(request)
    if (user == None): return

    company: Company = Company.query.filter_by(id=company_id).first_or_404()

    company.categories.clear()
    db.session.commit()

    db.session.delete(company)
    db.session.commit()

    return "", 200

def throwIfNotAdmin(request_) -> User:
    isAuth = authenticate(request_)
    
    if not isAuth.isAuthenticated:
        abort(403)
        return None
    
    userId = isAuth.session.user_id

    user: User = User.query.filter_by(id=userId).first_or_404()

    if not isAdmin(user):
        abort(403)
        return None
    
    return user