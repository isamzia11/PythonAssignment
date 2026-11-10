# Name Isam Zia Roll no: TRN-2026-00346 

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative")


products = [
    Product("Laptop", 120000, 5, ["electronics"]),
    Product("Mouse", 1500, 0, ["accessories"]),
    Product("Keyboard", 3500, 10, ["accessories"]),
    Product("Monitor", 30000, 0, ["electronics"]),
    Product("USB Cable", 500, 20, ["cables"])
]

print("===== OUT OF STOCK PRODUCTS =====")

for product in products:
    if product.stock == 0:
        print(f"{product.name} - Rs {product.price}")
