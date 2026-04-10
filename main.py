
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("GAMING WORK LAPTOP", 1800, 1)
p2 = Product("Telefon", 500, 3)

manager.add_product(p1)
manager.add_product(p2)

manager.show_products()
print("Ukupna vrednost:", manager.total_value())

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

print("KORPA:")
cart.show_cart()
print("UKUPNO:", cart.total_price())