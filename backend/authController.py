from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from authHandler import authenticate
from models import User, Session, db
from validator import registerValidation
import datetime

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')

    if not email or not password or not firstname or not lastname:
        return jsonify({'error': 'Brak wymaganych danych rejestracji (email, password, firstname, lastname)'}), 400

    validData = registerValidation(email, password, firstname, lastname)
    if not validData:
        return jsonify({'error': 'Nieprawidłowe dane rejestracji'}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'error': 'Użytkownik z tym email już istnieje'}), 409

    passwordHash = generate_password_hash(password.strip())
    newUser = User(
            email=email.strip(),
            password=passwordHash,
            firstname=firstname.strip(),
            lastname=lastname.strip()
    )
    db.session.add(newUser)
    db.session.commit()

    return jsonify({'message': 'Rejestracja udana'}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Brak nazwy użytkownika lub hasła'}), 400

    user: User | None = User.query.filter_by(email=email.strip()).first()
    if user == None or not check_password_hash(user.password, password.strip()):
        return jsonify({'error': 'Nieprawidłowe dane logowania'}), 401

    session_id = str(uuid.uuid4())

    datetime_now = datetime.datetime.now()
    session_expiry = datetime_now + datetime.timedelta(days=14)

    newSession = Session(
            session_id=session_id, 
            user_id=user.id,
            expires_at=session_expiry,
            userAgent=request.headers.get('User-Agent')
            )

    db.session.add(newSession)
    db.session.commit()

    resp = make_response(jsonify({'message': 'Logowanie udane'}), 200)
    resp.set_cookie('session_id', session_id, httponly=True, samesite=None, expires=session_expiry)
    return resp


@auth.route('/logout', methods=['POST'])
def logout():
    isAuth = authenticate(request)

    if not isAuth.isAuthenticated:
        return jsonify({'error': 'Brak aktywnej sesji'}), 401
    
    Session.query.filter_by(session_id=isAuth.session.session_id).delete()
    db.session.commit()
    
    resp = make_response(jsonify({'message': 'Wylogowano pomyślnie'}), 200)
    resp.set_cookie('session_id', '', expires=0)
    return resp
