class Book:
    def __init__(self, id, title, author, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"