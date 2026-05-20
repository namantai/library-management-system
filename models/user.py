from models.person import Person

class User(Person):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__history = []

    def add_history(self, action):
        self.__history.append(action)

    def get_history(self):
        return self.__history