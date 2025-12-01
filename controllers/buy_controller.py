from bottle import Bottle, request
from .base_controller import BaseController
from services.buy_service import BuyService
from models.user import User

class BuyController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.buy_service = BuyService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/buy/<product_id:int>', method=['GET', 'POST'], callback=self.buy_product)
        self.app.route('/buy/receipt/<buy_id:int>', method='GET', callback=self.receipt)
        self.app.route('/sahur.buys', method='GET', callback=self.list_buys)

    def buy_product(self, product_id):
        

        product = self.buy_service.product_model.get_by_id(product_id)
        if not product:
            return "Produto não encontrado."

        if request.method == 'GET':
            return self.render('buy_form', product=product, action=f'/buy/{product_id}')

        
        email = request.forms.get('email')
        password_crua = request.forms.get('password')
        nick = request.forms.get('nick')

        password = User.set_password(password_crua)

        buy = self.buy_service.create_buy(product_id, email, password, nick)

        if not buy:
            return self.render('buy_form', product=product, action=f'/buy/{product_id}', error="Erro na compra.")

        
        return self.redirect(f'/buy/receipt/{buy.id}')

    def receipt(self, buy_id):
        buy = self.buy_service.get_by_id(buy_id)
        if not buy:
            return "Compra não encontrada."

        product = self.buy_service.product_model.get_by_id(buy.product_id)
        return self.render('buy_receipt', buy=buy, product=product)

    def list_buys(self):
        buys = self.buy_service.get_all_buys()
        return self.render('buy_list', buys=buys)

buy_routes = Bottle()
buy_controller = BuyController(buy_routes)