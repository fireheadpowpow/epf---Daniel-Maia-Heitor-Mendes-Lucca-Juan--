from bottle import Bottle, request
from .base_controller import BaseController
from services.product_services import ProductService

class ProductController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        
        self.setup_routes()
        self.product_service = ProductService()

    
    
    def setup_routes(self):
        self.app.route('/sahurproducts', method='GET', callback=self.list_products)
        self.app.route('/products/add', method=['GET', 'POST'], callback=self.add_product)
        self.app.route('/products/edit/<product_id:int>', method=['GET', 'POST'], callback=self.edit_product)
        self.app.route('/products/delete/<product_id:int>', method='POST', callback=self.delete_products)

    def list_products(self):
        products = self.product_service.get_all()
        return self.render('products', products=products)

    def add_product(self):
        if request.method == 'GET':
            return self.render('product_form', product=None, action='/products/add')
        else:
            self.product_service.save()
            self.redirect('/sahurproducts')

    def edit_product(self, product_id):
        product = self.product_service.get_by_id(product_id)

        if not product:
            return "Produto não encontrado"
        
        if request.method == 'GET':
            return self.render('product_form', product=product, action=f'/products/edit/{product_id}')
        else:
            self.product_service.edit(product)
            self.redirect('/sahurproducts')

    def delete_products(self, product_id):
        self.product_service.delete(product_id)
        self.redirect('/sahurproducts')

product_routes = Bottle()
product_controller = ProductController(product_routes)