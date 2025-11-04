from app.models.base_model import BaseModel
from app.extensions import db

class Amenity(BaseModel):
    """Amenity model for database persistence"""
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
        """Initialize a new amenity with a validated name"""
        super().__init__()
        self.name = self.validate_name(name)

    def validate_name(self, name):
        """Validate that the amenity name is a non-empty string within length limits"""
        if not name or not isinstance(name, str):
            raise ValueError("Amenity name is required and must be a string")
        if len(name) > 50:
            raise ValueError("Amenity name must not exceed 50 characters")
        return name
