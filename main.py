from services.library_service import LibraryService

def main():
    service = LibraryService()

    while True:
        print("\n Library Management System ")
        print("1. Show books")
        print("2. Add book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Show user history")
        print("6. Show statistics")
        print("7. Exit")

        choice = input("Choose option: ")

        try:
            if choice == "1":
                service.show_available_books()

            elif choice == "2":
                title = input("Enter title: ")
                author = input("Enter author: ")
                service.add_book(title, author)

            elif choice == "3":
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                service.borrow_book(user_id, book_id)

            elif choice == "4":
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                service.return_book(user_id, book_id)

            elif choice == "5":
                user_id = int(input("Enter user ID: "))
                service.show_user_history(user_id)

            elif choice == "6":
                service.show_statistics()

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid option")

        except ValueError:
            print("Please enter correct values")

if __name__ == "__main__":
    main()