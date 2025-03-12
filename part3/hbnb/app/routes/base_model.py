from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base qui est utilisée pour la création de tous les modèles SQLAlchemy
Base = declarative_base()

class BaseModel:
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
