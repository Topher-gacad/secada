from models.db import db
from datetime import datetime, timezone

class UserProfile(db.Model):
    __tablename__ = 'user_profile'

    id = db.Column(db.Integer, primary_key=True)

    user_auth_id = db.Column(db.Integer, db.ForeignKey('user_auth.id'), unique=True, nullable=False)
    user_auth = db.relationship('UserAuth', back_populates='user_profile')

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)
    department = db.relationship('Department', back_populates='user_profiles')

    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    theme_mode = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<UserProfile {self.fname} {self.lname}>'