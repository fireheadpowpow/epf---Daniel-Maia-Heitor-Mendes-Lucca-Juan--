import json
import os
from dataclasses import dataclass, asdict
from typing import List
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
class Buy:
    def __init__(self, id, product_id, email, nick, date):
        self.id = id
        self.product_id = product_id
        self.email = email
        self.nick = nick
        self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'email': self.email,
            'nick': self.nick,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class BuyModel:
    FILE_PATH = os.path.join(DATA_DIR, 'buy.json')

    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.buys = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return [Buy(**item) for item in data]
            except json.JSONDecodeError:
                
                return []

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([b.to_dict() for b in self.buys], f, indent=4, ensure_ascii=False)

    def add(self, buy: Buy):
        self.buys.append(buy)
        self._save()

    def get_all(self):
        return self.buys