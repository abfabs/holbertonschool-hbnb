from app.models.basemodel import BaseModel
from app.models.associations import place_amenity
from app.extensions import db

class Place(BaseModel):
    __tablename__ = 'places'
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    owner = db.relationship('User', backref='places')
    amenities = db.relationship('Amenity', secondary=place_amenity, backref='places', lazy=True)
    
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner_id = owner_id
    
    def validate_title(self, title):
        """Validate that the title is a non-empty string within length limits"""
        if not title or not isinstance(title, str):
            raise ValueError("Title is required and must be a string")
        if len(title) > 100:
            raise ValueError("Title must not exceed 100 characters")
        return title
    
    def validate_price(self, price):
        """Validate that the price is a positive number"""
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be a positive value")
        return float(price)
    
    def validate_latitude(self, latitude):
        """Validate that the latitude is a number within valid geographic range"""
        if not isinstance(latitude, (int, float)):
            raise ValueError("Latitude must be a number")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return float(latitude)
    
    def validate_longitude(self, longitude):
        """Validate that the longitude is a number within valid geographic range"""
        if not isinstance(longitude, (int, float)):
            raise ValueError("Longitude must be a number")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return float(longitude)
