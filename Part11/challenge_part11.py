# Name Isam Zia Roll no: TRN-2026-00346 

import json
from dataclasses import dataclass, field, asdict


@dataclass(order=True)
class Product:
    price: float
    name: str = field(compare=False)
    stock: int = field(compare=False)
    tags: list[str] = field(
        default_factory=list,
        compare=False
    )

    def __post_init__(self):
        if self.price < 0 or self.stock < 0:
            raise ValueError("Negative price or stock")


products = [
    Product(120000, "Laptop", 5),
    Product(1500, "Mouse", 0),
    Product(3500, "Keyboard", 10),
    Product(30000, "Monitor", 0),
    Product(500, "USB Cable", 20)
]

# Save products
data = [asdict(product) for product in products]

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Products saved!")

# Load products
with open("products.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

loaded_products = [
    Product(**item) for item in loaded_data
]

# Sort by price using dataclass ordering
sorted_products = sorted(loaded_products)

print("\n===== PRODUCTS BY PRICE =====")

for product in sorted_products:
    print(f"{product.name}: Rs {product.price}")
