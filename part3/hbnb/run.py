from flask import Flask
from app.routes.auth import auth_bp
from app.routes.places import places_bp
from app.routes.reviews import reviews_bp
from app.routes.users import users_bp

app = Flask(__name__)

# Enregistrement des routes
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(places_bp, url_prefix="/api")
app.register_blueprint(reviews_bp, url_prefix="/api")
app.register_blueprint(users_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
