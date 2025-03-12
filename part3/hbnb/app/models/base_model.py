from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app import db
import uuid
from datetime import datetime


# Base qui est utilisée pour la création de tous les modèles SQLAlchemy
Base = declarative_base()

class BaseModel(db.Model):
    __abstract__ = True  # This ensures SQLAlchemy does not create a table for BaseModel
    """Classe de base avec des méthodes communes à tous les modèles"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)

    def save(self):
        """Sauvegarder l'objet dans la base de données"""
        from app.storage import storage
        storage.save(self)
    
    def to_dict(self):
        """Convertir l'objet en dictionnaire"""
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
