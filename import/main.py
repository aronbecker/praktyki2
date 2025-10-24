import os
import sys
import requests

from .create_db_scheme import run_flask_migrations
from .create_database import create_database, create_env_file

def main():
    os.chdir("import")
    if "-init" in sys.argv:
        db_name = create_database()
        create_env_file(f"mysql://root:@localhost/{db_name}")
        run_flask_migrations()
        print(f"Struktura bazy danych pomyślnie stworzona ✅")
    elif "-data" in sys.argv:
        requests.get("http://127.0.0.1:1500/import")
        print("Dane zostały za importowane ✅")

if __name__ == "__main__":
    main()