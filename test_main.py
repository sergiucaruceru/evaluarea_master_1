from main import add_numbers, validate_message

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_validate_message():
    assert validate_message("Salut") is True
    assert validate_message("   ") is False