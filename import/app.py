import sys
from dotenv import load_dotenv
from backend.models import *
from backend.models.extensions import db
from flask import Flask, request
import pymysql
from flask_migrate import Migrate
import os
from .import_companies import import_aktywne_firmy
from .import_categories import import_kategori

load_dotenv()

pymysql.install_as_MySQLdb()

app = Flask(__name__)

database_uri =  os.getenv('db_URI')
if not database_uri:
    raise RuntimeError("db_URI is not set in environment variables.")

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.init_app(app)

migrate = Migrate(app, db)

@app.route("/import")
def impCompanies():
    os.chdir("import")
    data = import_aktywne_firmy()
    import_kategori(data)
    return "", 200


if __name__ == '__main__':
    app.run(debug=True, port=1500)