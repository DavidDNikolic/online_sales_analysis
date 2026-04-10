
from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1000, 2)
p2 = Product("Telefon", 500, 3)

manager.add_product(p1)
manager.add_product(p2)

manager.show_products()
print("Ukupna vrednost:", manager.total_value())
from cart import Cart

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)

print("KORPA:")
cart.show_cart()
print("UKUPNO:", cart.total_price())