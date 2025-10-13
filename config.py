import os


# Base configuration class with default settings for the application
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False


# Development environment configuration with debug mode enabled
class DevelopmentConfig(Config):
    DEBUG = True


# Configuration dictionary mapping environment names to config classes
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
