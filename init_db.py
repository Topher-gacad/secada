from sqlalchemy.engine.url import make_url
from mysql.connector import Error
from config import Config
import mysql.connector

def create_db_if_not_exists():
    try: 
        url = make_url(Config.SQLALCHEMY_DATABASE_URI)
        if url.get_backend_name() != "mysql":
            print("Only MYSQL is supported by this script")
            return False
        user = url.username or ""
        password = url.password or ""
        host = url.host or "localhost"
        port = url.port or 3306
        database = url.database

        if not database:
            print("No database name is SQLALCHEMY_DATABASE_URI")
            return False
        db_conn = mysql.connector.connect(host=host, user=user, password=password, port=port)
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{database}` "
            f"CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        print(f"Database `{database}` is ready! ")
        db_cursor.close(); db_conn.close()
        return True
    except Error as e:
        print(f"MYSQL Error: {e}")
        return False
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")
        return False
    
if __name__ == "__main__":
    ok = create_db_if_not_exists()
    print("Success" if ok else "Failed")
