import os
import requests

def main():
    os.chdir("import")
    # db_name = create_database()
    # create_env_file(f"mysql://root:@localhost/{db_name}")
    # run_flask_migrations()
    requests.get("http://127.0.0.1:1500/import")


if __name__ == "__main__":
    main()