import mysql.connector
from mysql.connector import Error
import os

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if not connection.is_connected():
            print("❌ Nie udało się połączyć z MySQL.")
            return

        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        existing_dbs = [row[0].lower() for row in cursor.fetchall()] 

        base_name = "firmaSkoki"
        new_db = base_name
        counter = 2
        while new_db.lower() in existing_dbs:
            new_db = f"{base_name}{counter}"
            counter += 1

        cursor.execute(f"CREATE DATABASE `{new_db}`")
        connection.commit()

        print(f"✅ Utworzono bazę danych: {new_db}")
        return new_db

    except Error as e:
        print(f"❌ Błąd MySQL: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def create_env_file(db_uri: str):
    """
    Tworzy plik .env jeśli nie istnieje, 
    a jeśli istnieje, nadpisuje go zmienną db_URI.
    """
    env_content = f"db_URI={db_uri}\n"
    with open(".env", "w") as env_file:
        env_file.write(env_content)
    print("✅ Plik .env został utworzony/aktualizowany.")


