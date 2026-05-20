from services.file_service import load_data, save_data

def show_available_books():
    books = load_data("books.json")

    print("\nAvailable Books:")
    for book in books:
        if book["available"]:
            print(f'{book["id"]}. {book["title"]}')


def borrow_book(user_id, book_id):
    books = load_data("books.json")
    users = load_data("users.json")

    for book in books:
        if book["id"] == book_id:

            if not book["available"]:
                print("Book is unavailable")
                return

            for user in users:
                if user["user_id"] == user_id:

                    if book_id in user["borrowed_books"]:
                        print("Already borrowed")
                        return

                    book["available"] = False
                    user["borrowed_books"].append(book_id)
                    user["history"].append(f"Borrowed book {book_id}")

                    save_data("books.json", books)
                    save_data("users.json", users)

                    print("Book borrowed successfully")
                    return


def return_book(user_id, book_id):
    books = load_data("books.json")
    users = load_data("users.json")

    for book in books:
        if book["id"] == book_id:
            for user in users:
                if user["user_id"] == user_id:

                    if book_id not in user["borrowed_books"]:
                        print("Book was not borrowed")
                        return

                    book["available"] = True
                    user["borrowed_books"].remove(book_id)
                    user["history"].append(f"Returned book {book_id}")

                    save_data("books.json", books)
                    save_data("users.json", users)

                    print("Book returned successfully")
                    return