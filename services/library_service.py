from services.file_service import FileService

class LibraryService:
    def __init__(self):
        self.books_file = "books.json"
        self.users_file = "users.json"

    def add_book(self, title, author):
        books = FileService.load(self.books_file)
        new_id = len(books) + 1

        books.append({
            "id": new_id,
            "title": title,
            "author": author,
            "available": True
        })

        FileService.save(self.books_file, books)
        print("Book added")

    def show_available_books(self):
        books = FileService.load(self.books_file)

        available = filter(lambda b: b["available"], books)

        for book in available:
            print(f'{book["id"]}: {book["title"]}')

    def borrow_book(self, user_id, book_id):
        books = FileService.load(self.books_file)
        users = FileService.load(self.users_file)

        for book in books:
            if book["id"] == book_id:
                if not book["available"]:
                    print("Unavailable")
                    return

                for user in users:
                    if user["user_id"] == user_id:
                        borrowed = set(user["borrowed_books"])

                        if book_id in borrowed:
                            print("Already borrowed")
                            return

                        book["available"] = False
                        user["borrowed_books"].append(book_id)
                        user["history"].append(f"Borrowed {book_id}")

                        FileService.save(self.books_file, books)
                        FileService.save(self.users_file, users)

                        print("Success")
                        return

    def return_book(self, user_id, book_id):
        books = FileService.load(self.books_file)
        users = FileService.load(self.users_file)

        for book in books:
            if book["id"] == book_id:
                for user in users:
                    if user["user_id"] == user_id:
                        if book_id not in user["borrowed_books"]:
                            print("Not borrowed")
                            return

                        book["available"] = True
                        user["borrowed_books"].remove(book_id)
                        user["history"].append(f"Returned {book_id}")

                        FileService.save(self.books_file, books)
                        FileService.save(self.users_file, users)

                        print("Returned")
                        return

    def show_user_history(self, user_id):
        users = FileService.load(self.users_file)

        for user in users:
            if user["user_id"] == user_id:
                for action in user["history"]:
                    print(action)