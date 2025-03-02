from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating if 1 <= rating <= 5 else 3  # Valeur par défaut de 3 si invalide
        self.place = place
        self.user = user
