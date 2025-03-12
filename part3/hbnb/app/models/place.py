from app.storage import storage
from app.models.base import BaseModel  # Assure-toi d'avoir un modèle de base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel):
    __tablename__ = 'places'

    title = Column(String(128), nullable=False)
    description = Column(String(1024))
    price = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Relation avec User (propriétaire du lieu)
    owner = relationship('User', back_populates='places')

    # Relation avec Review (les avis liés au lieu)
    reviews = relationship('Review', back_populates='place', cascade="all, delete-orphan")

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
