from app.storage import storage  
from app.routes.base_model import BaseModel  
from sqlalchemy import Column, String, Integer, ForeignKey  
from sqlalchemy.orm import relationship  
from flask import Blueprint, jsonify, request  
from app.routes.review import Review  

# Définition du Blueprint pour les routes des avis
review_bp = Blueprint('review', __name__)

# Route pour récupérer tous les avis
@review_bp.route('/', methods=['GET'])
def get_reviews():
    reviews = []
    return jsonify(reviews)

# Route pour créer un nouvel avis
@review_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()  # Récupère les données envoyées dans la requête POST
    review = Review(
        user_id=data["user_id"], 
        place_id=data["place_id"], 
        content=data["content"]
    )
    return jsonify({"message": "Review created", "review": review.to_dict()}), 201


# Définition du modèle Review
class Review(BaseModel):
    __tablename__ = 'reviews'

    # Définition des colonnes de la table 'reviews'
    text = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    # Définition des relations avec les autres modèles (User et Place)
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

    def to_dict(self):
        """Convertir l'objet en dictionnaire pour la réponse JSON"""
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id
        }
