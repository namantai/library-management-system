from utils.validators import validate_book_id


def test_valid_book_id():
    assert validate_book_id(1) == True


def test_invalid_book_id():
    assert validate_book_id(-5) == False