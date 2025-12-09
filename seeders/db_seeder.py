from app import app
from models import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from seeders.user_seeder import user_seed_data
from seeders.department_seeder import department_seed_data


def db_seeder():
    with app.app_context():
        try:
            print("Database Seeding Started...")
            print("Note: Make sure you've run migrations first!")
            print("  flask db init")
            print("  flask db migrate -m 'Initial migration'")
            print("  flask db upgrade")
            print("-" * 50)

            print("[1/2] Seeding Departments...")
            department_seed_data()

            print("[2/2] Seeding Users...")
            user_seed_data()

            print("Database Seeding Completed Successfully!")
        except IntegrityError as e: 
            db.session.rollback()
            print(f"Database Error: {e}")
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Unexpected Error: {e}")
        finally:
            db.session.close()

if __name__ == "__main__":
    db_seeder()
            