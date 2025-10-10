from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description  # Optional, no validation needed
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def validate_title(self, title):
        """Validate title: required, max 100 characters"""
        if not title or not isinstance(title, str):
            raise ValueError("Title is required and must be a string")
        if len(title) > 100:
            raise ValueError("Title must not exceed 100 characters")
        return title

    def validate_price(self, price):
        """Validate price: must be positive"""
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be a positive value")
        return float(price)

    def validate_latitude(self, latitude):
        """Validate latitude: must be between -90.0 and 90.0"""
        if not isinstance(latitude, (int, float)):
            raise ValueError("Latitude must be a number")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return float(latitude)

    def validate_longitude(self, longitude):
        """Validate longitude: must be between -180.0 and 180.0"""
        if not isinstance(longitude, (int, float)):
            raise ValueError("Longitude must be a number")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return float(longitude)

    def validate_owner(self, owner):
        """Validate owner: must be a User instance"""
        from app.models.user import User
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")
        return owner

    def add_review(self, review):
        """Add a review to the place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place"""
        from app.models.amenity import Amenity
        if not isinstance(amenity, Amenity):
            raise ValueError("Amenity must be a valid Amenity instance")
        if amenity not in self.amenities:
            self.amenities.append(amenity)
