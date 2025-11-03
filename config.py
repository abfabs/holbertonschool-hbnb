import os
from datetime import timedelta

# Base configuration class with default settings for the application
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default-jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    DEBUG = False

# Development environment configuration with debug mode enabled
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///development.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration dictionary mapping environment names to config classes
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
