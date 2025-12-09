from app import app
from models import db, UserAuth, UserProfile, Department
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def user_seed_data():
    with app.app_context():
        try: 
            print("Starting User Accounts Seeding...")
            
            it_dept = Department.query.filter_by(code="00").first()
            qual_dept = Department.query.filter_by(code="63").first()

            seed_users = [
                { 
                    "username" : "jdelacruz",
                    "email" : "jdelacruz@example.com",
                    "password" : "admin123",
                    "fname" : "Juan",
                    "lname" : "Dela Cruz",
                    "department" : it_dept
                },
                { 
                    "username" : "jmauie",
                    "email" : "jmauie@example.com",
                    "password" : "admin123",
                    "fname" : "John",
                    "lname" : "Mauie",
                    "department" : qual_dept
                },
            ]

            for user_data in seed_users:
                existing_user = UserAuth.query.filter_by(email=user_data['email']).first()
                if existing_user:
                    print(f"Skipping existing user: {user_data['email']}")
                    continue
                user_auth = UserAuth(
                    username = user_data["username"],
                    email= user_data["email"],
                    password_hash = generate_password_hash(user_data["password"])
                )
                db.session.add(user_auth)
                db.session.flush()

                user_profile = UserProfile(
                    user_auth_id=user_auth.id,
                    fname = user_data["fname"],
                    lname = user_data["lname"],
                    department_id = user_data["department"].id if user_data["department"] else None,
                    theme_mode=False
                )
                db.session.add(user_profile)

            db.session.commit()
            print(f"{len(seed_users)} users seeded successfully!")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity Error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLALchemy Error: {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected Error during Seeding: {e}")
        finally:
            db.session.close()
            print("Database session closed")

if __name__ == "__main__":
    user_seed_data()