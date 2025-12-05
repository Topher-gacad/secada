from models.db import db
from datetime import datetime, timezone


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationship: One department has many user profiles
    user_profile = db.relationship('UserProfile', back_populates='department', lazy='dynamic')

    def __repr__(self):
        return f'<Department {self.code}: {self.name}>'

