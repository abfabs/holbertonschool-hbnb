import logging
from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from app.extensions import bcrypt, jwt, db
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns


# Disable SQLAlchemy logging
logging.getLogger('sqlalchemy.engine').disabled = True


# Create and configure the Flask application with API namespaces
def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_ECHO'] = False

    # Initialize extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # Enable CORS for frontend
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    
    # Create API instance
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/docs')

    # Register namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    return app
