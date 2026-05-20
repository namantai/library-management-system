from utils.validators import validate_positive_id

def test_valid_id():
    assert validate_positive_id(1) == True

def test_invalid_id():
    assert validate_positive_id(-1) == False