from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner: User):
        super().__init__()
        self.title = title
        self.description = description
        self.price = float(price) if price >= 0 else 0.0
        self.latitude = latitude if -90.0 <= latitude <= 90.0 else 0.0
        self.longitude = longitude if -180.0 <= longitude <= 180.0 else 0.0
        self.owner = owner  # Référence vers un objet User
        self.reviews = []  # Liste des avis liés au lieu
        self.amenities = []  # Liste des commodités associées

    def add_review(self, review):
        """Ajoute un avis à ce lieu."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute une commodité à ce lieu."""
        self.amenities.append(amenity)
