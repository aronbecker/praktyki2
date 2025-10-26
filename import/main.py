import os
from flask import Flask
from .import_companies import import_glowny
from backend.models.extensions import db
import pymysql
import sys

def main():
    os.chdir("import/data")
    pymysql.install_as_MySQLdb()

    if len(sys.argv) < 2:
        raise Exception("❌ Nazwa bazy danych nie podana (sprawdź readme)")

    db_name = sys.argv[1]

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/" + db_name
    db.init_app(app)

    with app.app_context():
        for (_,_,files) in os.walk('.',topdown=True):
            for f in files:
                if f.endswith(".xlsx"):
                    print(f"Znaleziono plik z danymi - {f}")
                    import_glowny(f)

if __name__ == "__main__":
    main()