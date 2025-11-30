import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
class Product:
    def __init__(self, id, name, price, quantity, description, images = None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.images = images or []
        

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description,
            'images': self.images
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class ProductModel:
    FILE_PATH = os.path.join(DATA_DIR, 'products.json')

    def __init__(self):
        self.products = self._load()

    def _load(self):
        import json, os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            return [Product.from_dict(item) for item in json.load(f)]

    def _save(self):
        import json
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.products], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.products

    def get_by_id(self, products_id):
        return next((a for a in self.products if a.id == products_id), None)

    def add(self, product):
        self.products.append(product)
        self._save()

    def update(self, updated_product):
        for i, a in enumerate(self.products):
            if a.id == updated_product.id:
                self.products[i] = updated_product
                self._save()
                break

    def delete(self, products_id):
        self.products = [a for a in self.products if a.id != products_id]
        self._save()