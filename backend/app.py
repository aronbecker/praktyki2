import os
from dotenv import load_dotenv
from models import *
from models.extensions import db
from flask import Flask
import pymysql
from flask_migrate import Migrate

load_dotenv()


pymysql.install_as_MySQLdb()

app = Flask(__name__)

database_uri =  os.getenv('db_URI')
if not database_uri:
    raise RuntimeError("DATABASE_URI is not set in environment variables.")

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)

