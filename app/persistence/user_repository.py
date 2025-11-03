from app.persistence.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """Repository for User-specific database operations"""
    
    def __init__(self):
        from app.models.user import User
        super().__init__(User)

    def get_user_by_email(self, email):
        """Retrieve a user by their email address"""
        return self.model.query.filter_by(email=email).first()
