from app.models.user import User
from app.repositories.in_memory_repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Créer un nouvel utilisateur"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Obtenir un utilisateur par ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Obtenir un utilisateur par email"""
        return self.user_repo.get_by_attribute('email', email)
