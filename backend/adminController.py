from flask import Blueprint
from models import Company, User, Address, Category, db
from flask import request, abort
from authHandler import authenticate, isAdmin

admin = Blueprint('admin', __name__)


@admin.route('/admin/addCompany', methods=['POST'])
def addCompany():
    isAuth = authenticate(request)
    
    if not isAuth.isAuthenticated:
        return abort(403)
    
    userId = isAuth.session.user_id

    print("Test")
    user: User = User.query.filter_by(id=userId).first_or_404()

    if not isAdmin(user):
        return abort(403)

    data = request.get_json()

    name = data.get('name')
    ownerName = data.get('ownerName')
    phoneNumber = data.get("phoneNumber")
    email = data.get("email")
    website = data.get("website")
    categories = data.get("categories")
    town = data.get("town")
    street = data.get("street")
    building_number = data.get("building_number")
    apartment_number = data.get("apartment_number")

    addres = Address(
        town,
        street,
        building_number,
        apartment_number
    )

    categoriesEntities = []

    for name in categories:
        category = Category.query.filter_by(name=name).first()
        if not category:
            category = Category(name=name)
        categoriesEntities.append(category)

    company = Company(
        name,
        phoneNumber,
        email,
        ownerName,
        website,
    )


    company.categories = categoriesEntities
    company.address = addres

    db.session.add(company)
    db.session.commit()

    return "", 200
