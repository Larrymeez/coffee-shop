class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        from order import Order  # Local import to avoid circular dependency
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        max_spent = 0
        best_customer = None
        for customer in cls.all_customers:
            total = sum(order.price for order in Order.all_orders
                        if order.customer == customer and order.coffee == coffee)
            if total > max_spent:
                max_spent = total
                best_customer = customer
        return best_customer