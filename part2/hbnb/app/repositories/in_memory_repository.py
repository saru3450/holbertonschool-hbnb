class InMemoryRepository:
    def __init__(self):
        self.users = {}

    def add(self, user):
        self.users[user.id] = user

    def get(self, user_id):
        return self.users.get(user_id)

    def get_by_attribute(self, attribute, value):
        for user in self.users.values():
            if getattr(user, attribute) == value:
                return user
        return None
