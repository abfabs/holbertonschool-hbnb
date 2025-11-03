from app.persistence.repository import SQLAlchemyRepository


class PlaceRepository(SQLAlchemyRepository):
    """Repository for Place-specific database operations"""
    
    def __init__(self):
        from app.models.place import Place
        super().__init__(Place)

    def get_places_by_owner(self, owner_id):
        """Retrieve all places owned by a specific user"""
        return self.model.query.filter_by(owner_id=owner_id).all()

    def get_places_by_price_range(self, min_price, max_price):
        """Retrieve places within a specific price range"""
        return self.model.query.filter(
            self.model.price >= min_price,
            self.model.price <= max_price
        ).all()
