from services.file_service import FileService
from utils.validators import validate_positive_id
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
        print("Book added successfully")

    def show_available_books(self):
        books = FileService.load(self.books_file)

        available = filter(lambda b: b["available"], books)

        print("\nAvailable Books:")
        for book in available:
            print(f'{book["id"]}: {book["title"]} by {book["author"]}')

    def borrow_book(self, user_id, book_id):
        if not validate_positive_id(user_id) or not validate_positive_id(book_id):
            print("Invalid user_id or book_id")
            return
        books = FileService.load(self.books_file)
        users = FileService.load(self.users_file)

        for book in books:
            if book["id"] == book_id:

                if not book["available"]:
                    print("Book is unavailable")
                    return

                for user in users:
                    if user["user_id"] == user_id:

                        borrowed = set(user["borrowed_books"])

                        if book_id in borrowed:
                            print("Book already borrowed")
                            return

                        book["available"] = False
                        user["borrowed_books"].append(book_id)
                        user["history"].append(f"Borrowed book {book_id}")

                        FileService.save(self.books_file, books)
                        FileService.save(self.users_file, users)

                        print("Book borrowed successfully")
                        return

        print("User or book not found")

    def return_book(self, user_id, book_id):
        if not validate_positive_id(user_id) or not validate_positive_id(book_id):
            print("Invalid user_id or book_id")
            return
        books = FileService.load(self.books_file)
        users = FileService.load(self.users_file)

        for book in books:
            if book["id"] == book_id:

                for user in users:
                    if user["user_id"] == user_id:

                        if book_id not in user["borrowed_books"]:
                            print("This book was not borrowed")
                            return

                        book["available"] = True
                        user["borrowed_books"].remove(book_id)
                        user["history"].append(f"Returned book {book_id}")

                        FileService.save(self.books_file, books)
                        FileService.save(self.users_file, users)

                        print("Book returned successfully")
                        return

        print("User or book not found")

    def show_user_history(self, user_id):
        if not validate_positive_id(user_id):
            print("Invalid user_id")
            return
        users = FileService.load(self.users_file)

        for user in users:
            if user["user_id"] == user_id:
                print("\nUser History:")
                for action in user["history"]:
                    print(action)
        print("User not found")

    def show_statistics(self):
        books = FileService.load(self.books_file)
        users = FileService.load(self.users_file)

        total_books = len(books)
        available_books = len(list(filter(lambda b: b["available"], books)))
        borrowed_books = total_books - available_books
        total_users = len(users)

        print("\nLibrary Statistics")
        print(f"Total books: {total_books}")
        print(f"Available books: {available_books}")
        print(f"Borrowed books: {borrowed_books}")
        print(f"Registered users: {total_users}")
