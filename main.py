
from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop PRO", 1200, 1)
p2 = Product("Telefon MAX", 700, 2)

manager.add_product(p1)
manager.add_product(p2)

manager.show_products()
print("Ukupna vrednost:", manager.total_value())