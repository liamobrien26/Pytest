from lib.greet import greet

def test_greets_person():
    result = greet("Liam")

    assert result == "Hello, Liam!"
