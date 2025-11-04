from app.models.base_model import BaseModel
from app.extensions import db

class Review(BaseModel):
    """Review model for database persistence"""
    __tablename__ = 'reviews'

    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

        # Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)

    # Relationships
    user = db.relationship('User', backref='reviews', lazy=True)
    place = db.relationship('Place', backref='reviews', lazy=True)


    def __init__(self, text, rating, place=None, user=None):
        """Initialize a new review with validated attributes"""
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        if place:
            self.place = place  # SQLAlchemy will handle place_id
        if user:
            self.user = user  # SQLAlchemy will handle user_id


    def validate_text(self, text):
        """Validate that the review text is a non-empty string"""
        if not text or not isinstance(text, str):
            raise ValueError("Review text is required and must be a string")
        return text

    def validate_rating(self, rating):
        """Validate that the rating is an integer between 1 and 5"""
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating

    def update(self, data):
        """Update the review attributes with validation"""
        for key, value in data.items():
            if key == 'rating':
                value = self.validate_rating(value)
            elif key == 'text':
                value = self.validate_text(value)
            setattr(self, key, value)
        self.save()
