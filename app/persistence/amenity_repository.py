from app.persistence.repository import SQLAlchemyRepository


class AmenityRepository(SQLAlchemyRepository):
    """Repository for Amenity-specific database operations"""
    
    def __init__(self):
        from app.models.amenity import Amenity
        super().__init__(Amenity)

    def get_amenity_by_name(self, name):
        """Retrieve an amenity by its name"""
        return self.model.query.filter_by(name=name).first()
