from customer import Customer

def test_customer_name_validation():
    # Valid name
    c = Customer("Alice")
    assert c.name == "Alice"

    # Invalid: not a string
    try:
        Customer(123)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    # Invalid: too long
    try:
        Customer("A" * 16)
        assert False, "Expected ValueError"
    except ValueError:
        pass