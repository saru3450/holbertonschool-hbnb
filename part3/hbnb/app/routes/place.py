from sqlalchemy import Column, String, Float, ForeignKey  # Import des colonnes SQLAlchemy
from sqlalchemy.orm import relationship  # Import des relations SQLAlchemy
from flask import Blueprint, jsonify, request  # Import de Flask pour la gestion des routes
from app.routes.place import Place  # Import de la classe Place

# Définition du Blueprint pour les routes des lieux
place_bp = Blueprint('place', __name__)

# Route pour récupérer tous les lieux
@place_bp.route('/', methods=['GET'])
def get_places():
    places = []  # Logique pour récupérer les lieux depuis la base de données (à implémenter)
    return jsonify(places)

# Route pour créer un nouveau lieu
@place_bp.route('/', methods=['POST'])
def create_place():
    data = request.get_json()  # Récupère les données envoyées dans la requête POST
    place = Place(
        title=data["title"], 
        description=data["description"], 
        price=data["price"], 
        latitude=data["latitude"], 
        longitude=data["longitude"],
        owner_id=data["owner_id"]
    )
    # Logique pour ajouter le lieu à la base de données (à implémenter)
    return jsonify({"message": "Place created", "place": place.to_dict()}), 201


# Définition du modèle Place
class Place(BaseModel):
    __tablename__ = 'places'

    # Définition des colonnes de la table 'places'
    title = Column(String(128), nullable=False)
    description = Column(String(1024))
    price = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Définition des relations avec les autres modèles (User et Review)
    owner = relationship('User', back_populates='places')  # Relation avec le propriétaire (User)
    reviews = relationship('Review', back_populates='place', cascade="all, delete-orphan")  # Relation avec les avis (Review)

    def to_dict(self):
        """Convertir l'objet en dictionnaire pour la réponse JSON"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id
        }
