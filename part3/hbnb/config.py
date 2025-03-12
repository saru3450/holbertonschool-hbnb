class Config:
    """Base configuration class."""
    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False
    ENV = 'production'

class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    DEBUG = True
    ENV = 'testing'
