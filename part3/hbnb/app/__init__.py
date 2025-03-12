from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig  # Vérifie que le fichier config.py existe et contient DevelopmentConfig

# Initialiser les extensions
bcrypt = Bcrypt()
jwt = JWTManager()

# Importation des namespaces
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns

def create_app(config_class=DevelopmentConfig):
    """Initialise et configure l'application Flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation des extensions
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Création de l'API
    api = Api(app, version='1.0', title='HBnB API', description='API')

    # Enregistrement des namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
