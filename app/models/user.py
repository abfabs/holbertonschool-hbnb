from app.models.basemodel import BaseModel
from app.extensions import db

class User(BaseModel):
    __tablename__ = 'users'
    
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
    
    def validate_first_name(self, first_name):
        """Validate that first_name is a non-empty string within length limits"""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name is required and must be a string")
        if len(first_name) > 50:
            raise ValueError("First name must not exceed 50 characters")
        return first_name
    
    def validate_last_name(self, last_name):
        """Validate that last_name is a non-empty string within length limits"""
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name is required and must be a string")
        if len(last_name) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        return last_name
    
    def validate_email(self, email):
        """Validate that email is a valid email format"""
        if not email or not isinstance(email, str):
            raise ValueError("Email is required and must be a string")
        if '@' not in email or '.' not in email.split('@')[1]:
            raise ValueError("Email must be a valid email format")
        if len(email) > 120:
            raise ValueError("Email must not exceed 120 characters")
        return email
