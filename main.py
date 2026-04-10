
from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1000, 2)
p2 = Product("Telefon", 500, 3)

manager.add_product(p1)
manager.add_product(p2)

manager.show_products()
print("Ukupna vrednost:", manager.total_value())