from app.models.base_model import BaseModel
from app.extensions import db, bcrypt
import re
from sqlalchemy.orm import validates

class User(BaseModel):
    """User model for database persistence"""
    __tablename__ = 'user'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, is_admin=False, password=None):
        """Initialize a new user with validated attributes"""
        super().__init__()
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin        
        if password:
            self.hash_password(password)

    def validate_first_name(self, first_name):
        """Validate first name: required, max 50 characters"""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name is required and must be a string")
        if len(first_name) > 50:
            raise ValueError("First name must not exceed 50 characters")
        return first_name

    def validate_last_name(self, last_name):
        """Validate last name: required, max 50 characters"""
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name is required and must be a string")
        if len(last_name) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        return last_name

    def validate_email(self, email):
        """Validate email: required, proper format"""
        if not email or not isinstance(email, str):
            raise ValueError("Email is required and must be a string")
        # Basic email validation pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        return email

    @validates('first_name')
    def validate_first_name_sqlalchemy(self, key, first_name):
        """SQLAlchemy validator for first_name"""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name is required and must be a string")
        if len(first_name) > 50:
            raise ValueError("First name must not exceed 50 characters")
        return first_name

    @validates('last_name')
    def validate_last_name_sqlalchemy(self, key, last_name):
        """SQLAlchemy validator for last_name"""
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name is required and must be a string")
        if len(last_name) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        return last_name

    @validates('email')
    def validate_email_sqlalchemy(self, key, email):
        """SQLAlchemy validator for email"""
        if not email or not isinstance(email, str):
            raise ValueError("Email is required and must be a string")
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        return email

    def hash_password(self, password):
        """Hash the password before storing it"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password"""
        return bcrypt.check_password_hash(self.password, password)

    def add_place(self, place):
        """Add a place to the user's list of places"""
        self.places.append(place)
