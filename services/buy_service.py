from bottle import request
from datetime import datetime
from models.buy import Buy, BuyModel
from models.user import UserModel, User
from models.product import ProductModel

class BuyService:
    def __init__(self):
        self.buy_model = BuyModel()
        self.user_model = UserModel()
        self.product_model = ProductModel()

    def get_all(self):
        return self.buy_model.get_all()

    def create_buy(self, product_id, email, password, nick):
        
        password = User.set_password(password)
        user = self.user_model.get_by_email_password(email, password)
        if not user:
            return None

        product = self.product_model.get_by_id(product_id)
        if not product or product.quantity <= 0:
            return None

        
        last_id = max([b.id for b in self.buy_model.get_all()], default=0)
        new_id = last_id + 1

        
        buy = Buy(
            id=new_id,
            product_id=product_id,
            email=email,
            nick=nick,
            date=datetime.now().strftime("%d/%m/%Y %H:%M")
        )

        
        self.buy_model.add(buy)

        
        product.quantity -= 1
        self.product_model.update(product)

        self.product_model.reload()

        return buy

    def get_by_id(self, buy_id):
        return next((b for b in self.buy_model.get_all() if b.id == buy_id), None)

    def update(self, buy):
        self.buy_model.update(buy)

    def delete(self, buy_id):
        self.buy_model.delete(buy_id)
