from customer import Customer
from coffee import Coffee
from order import Order

# Customers
donald = Customer("Donald")
william = Customer("William")
macron = Customer("Macron")

# Coffee types
espresso = Coffee("Espresso")
latte = Coffee("Latte")
mochablast = Coffee("Mochablast")

# Orders
donald.create_order(espresso, 4.5)
donald.create_order(latte, 5.5)
william.create_order(espresso, 3.5)
macron.create_order(mochablast, 6.0)
macron.create_order(espresso, 4.0)

# Output checks
print("☕ Customers for Espresso:", [c.name for c in espresso.customers()])
print("🌟 Coffees Donald has ordered:", [c.name for c in donald.coffees()])
print("📊 Espresso order count:", espresso.num_orders())
print("💰 Average price for Espresso:", espresso.average_price())
