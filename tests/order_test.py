from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation_and_validation():
    c = Customer("Sam")
    cf = Coffee("Espresso")

    # Valid order
    o = Order(c, cf, 3.5)
    assert o.customer == c
    assert o.coffee == cf
    assert o.price == 3.5

    # Invalid price type
    try:
        Order(c, cf, "5.0")
        assert False, "Expected TypeError"
    except TypeError:
        pass

    # Invalid price range
    try:
        Order(c, cf, 0.5)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    # Invalid customer type
    try:
        Order("NotACustomer", cf, 3.0)
        assert False, "Expected TypeError"
    except TypeError:
        pass