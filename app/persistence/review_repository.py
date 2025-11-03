from app.persistence.repository import SQLAlchemyRepository


class ReviewRepository(SQLAlchemyRepository):
    """Repository for Review-specific database operations"""
    
    def __init__(self):
        from app.models.review import Review
        super().__init__(Review)

    def get_reviews_by_rating(self, rating):
        """Retrieve all reviews with a specific rating"""
        return self.model.query.filter_by(rating=rating).all()

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews for a specific place"""
        return self.model.query.filter_by(place_id=place_id).all()
