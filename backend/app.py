import os
from dotenv import load_dotenv
from models import *
from models.extensions import db
from flask import Flask
import pymysql
from flask_migrate import Migrate
from controller import page 
from authController import auth 
from flask_cors import CORS

load_dotenv()

pymysql.install_as_MySQLdb()

app = Flask(__name__)

database_uri =  os.getenv('db_URI')
if not database_uri:
    raise RuntimeError("db_URI is not set in environment variables.")

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(page)
app.register_blueprint(auth)

webAppUrl = os.getenv('webapp_URL')
originList = ["http://localhost:5173/"]
if webAppUrl:
    originList[0] = webAppUrl

CORS(app, supports_credentials=True, origins=originList)

if __name__ == '__main__':
    app.run(debug=True)
