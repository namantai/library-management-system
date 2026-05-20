def validate_positive_id(value):
    return isinstance(value, int) and value > 0