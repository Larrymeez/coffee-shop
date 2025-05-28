from coffee import Coffee

def test_coffee_name_validation():
    # Valid name
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

    # Invalid: not a string
    try:
        Coffee(123)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    # Invalid: too short
    try:
        Coffee("AB")
        assert False, "Expected ValueError"
    except ValueError:
        pass

    # Test immutability
    try:
        coffee.name = "Mocha"
        assert False, "Expected AttributeError"
    except AttributeError:
        pass