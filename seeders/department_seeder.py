from app import app
from models import db, Department
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def department_seed_data():
    with app.app_context():
        try:
            print("Starting Department Seeding...")

            seed_departments = [
                Department(
                    name = "MIS - IT",
                    code = "00" 
                ),  
                Department(
                    name = "Quality Assurance",
                    code = "63"
                ),
                  Department(
                    name = "Warehouse",
                    code = "84"
                ),
                  Department(
                    name = "Safety & Health Management",
                    code = "74"
                ),
                  Department(
                    name = "Customer Care & Warranty",
                    code = "75"
                ),
                  Department(
                    name = "Project Management",
                    code = "65"
                ),
            ]
            
            for department in seed_departments:
                existing_department = Department.query.filter_by(code=department.code).first()
                if existing_department:
                    print(f"Skipping existing department/s: {department.code}")
                    continue
                db.session.add(department)

            db.session.commit()
            print(f" {len(seed_departments)} departments seeded successfully!")
        
        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity Error: {e}")
        except SQLAlchemyError as e: 
            db.session.rollback()
            print(f"SQLAlchemy Error: {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected Error during Seeding: {e}")
        finally:
            db.session.close()
            print("Database session closed")

if __name__ == "__main__":
    department_seed_data()