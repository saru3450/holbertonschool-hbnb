from app.storage import storage
from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    # Relation avec User (auteur de l'avis)
    user = relationship('User', back_populates='reviews')

    # Relation avec Place (le lieu concerné)
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
