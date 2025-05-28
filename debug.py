from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")

# Create Orders using method
alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
bob.create_order(espresso, 2.5)
bob.create_order(espresso, 3.5)
charlie.create_order(cappuccino, 4.0)

# Print Customer Orders
print("\n--- Customer Orders ---")
for customer in [alice, bob, charlie]:
    print(f"{customer.name} ordered:")
    for order in customer.orders():
        print(f"  - {order.coffee.name} (${order.price})")
    print("Coffees ordered:", [coffee.name for coffee in customer.coffees()])
    print()

# Print Coffee Stats
print("\n--- Coffee Stats ---")
for coffee in [latte, espresso, cappuccino]:
    print(f"{coffee.name} has {coffee.num_orders()} orders.")
    print(f"Average price: ${coffee.average_price():.2f}")
    print("Customers who ordered:", [c.name for c in coffee.customers()])
    print()

# : Most Aficionado
print("\n--- Most Aficionado ---")
for coffee in [latte, espresso, cappuccino]:
    aficionado = Customer.most_aficionado(coffee)
    if aficionado:
        print(f"{aficionado.name} spent the most on {coffee.name}.")
    else:
        print(f"No orders for {coffee.name}.")