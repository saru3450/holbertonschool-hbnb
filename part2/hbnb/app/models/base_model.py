import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Initialise un objet avec un UUID et des timestamps."""
        self.id = str(uuid.uuid4())  # Génère un identifiant unique sous forme de string
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Met à jour le timestamp updated_at."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Met à jour les attributs d'un objet avec les valeurs d'un dictionnaire."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
