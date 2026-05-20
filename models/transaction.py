class Transaction:
    def __init__(self, user_id, book_id, action):
        self.user_id = user_id
        self.book_id = book_id
        self.action = action