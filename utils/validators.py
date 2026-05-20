def validate_book_id(book_id):
    return isinstance(book_id, int) and book_id > 0


def validate_user_name(name):
    return isinstance(name, str) and len(name.strip()) > 0