from models.person import Person

class User(Person):
    def __init__(self, user_id, name):
        super().__init__(name)
        self.user_id = user_id
        self.borrowed_books = []
        self.history = []