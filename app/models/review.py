from app.models.basemodel import BaseModel
from app.extensions import db

class Review(BaseModel):
    __tablename__ = 'reviews'
    
    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    
    # Relationships
    user = db.relationship('User', backref='reviews')
    place = db.relationship('Place', backref='reviews')
    
    def __init__(self, text, rating, user_id, place_id):
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.user_id = user_id
        self.place_id = place_id
    
    def validate_text(self, text):
        """Validate that the text is a non-empty string within length limits"""
        if not text or not isinstance(text, str):
            raise ValueError("Review text is required and must be a string")
        if len(text) > 500:
            raise ValueError("Review text must not exceed 500 characters")
        return text
    
    def validate_rating(self, rating):
        """Validate that the rating is between 1 and 5"""
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating
