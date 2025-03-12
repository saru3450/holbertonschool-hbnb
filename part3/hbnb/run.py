from flask import Flask
from app.routes.auth import auth_bp  # Import du Blueprint d'authentification
from app.routes.user import user_bp  # Import du Blueprint des utilisateurs
from app.routes.place import place_bp  # Import du Blueprint des lieux
from app.routes.review import review_bp  # Import du Blueprint des avis
from app.routes.amenity import amenity_bp  # Import du Blueprint des commodités

def create_app():
    """
    Crée et configure l'application Flask avec tous les Blueprints.
    """
    app = Flask(__name__)

    # Enregistrer les Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Les routes d'authentification seront sous '/auth'
    app.register_blueprint(user_bp, url_prefix='/user')  # Les routes des utilisateurs seront sous '/user'
    app.register_blueprint(place_bp, url_prefix='/place')  # Les routes des lieux seront sous '/place'
    app.register_blueprint(review_bp, url_prefix='/review')  # Les routes des avis seront sous '/review'
    app.register_blueprint(amenity_bp, url_prefix='/amenitie')  # Les routes des commodités seront sous '/amenitie'

    return app
