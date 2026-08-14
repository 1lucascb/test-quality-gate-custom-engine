from dataclasses import dataclass
from src.domain.product import Product

@dataclass
class Order:
    id: str
    products: list[Product]
