from bottle import Bottle, request
from .base_controller import BaseController
from services.product_services import ProductService


class ProductController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        
        self.setup_routes()
        self.product_service = ProductService()

    
    
    def setup_routes(self):
        self.app.route('/sahurhomepage', method='GET', callback=self.list_products)
        self.app.route('/products/add', method=['GET', 'POST'], callback=self.add_product)
        self.app.route('/products/edit/<product_id:int>', method=['GET', 'POST'], callback=self.edit_product)
        self.app.route('/products/delete/<product_id:int>', method='POST', callback=self.delete_products)
        self.app.route('/productsdetails/<product_id:int>', method='GET', callback=self.detail_products)

        

       
    
    def list_products(self):
        products = self.product_service.get_all()
        return self.render('home', products=products)

    def add_product(self):
        action_url = '/products/add'
        
        if request.method == 'GET':
            return self.render('product_form', product=None, action=action_url, error=None)
        
        try:
            self.product_service.create_product(self.product_model, request.forms, request.files)
            return self.redirect('/sahurhomepage')

        except (ValueError, TypeError) as e:
            context = {
                'action': action_url, 
                'product': None,
                'error': str(e)
            }
            return self.render('product_form', **context)

        except Exception as e:
            return f"Erro Inesperado no Servidor: {e}"
            

    def edit_product(self, product_id):
        product = self.product_service.get_by_id(product_id)

        if not product:
            return "Produto não encontrado"
        
        if request.method == 'GET':
            return self.render('product_form', product=product, action=f'/products/edit/{product_id}')
        else:
            self.product_service.edit(product)
            self.redirect('/sahurhomepage')

    def delete_products(self, product_id):
        self.product_service.delete(product_id)
        self.redirect('/sahurhomepage')

    
    def detail_products(self, product_id):
        mensagem_status = "O Produto não está mais disponível em estoque"
        product = self.product_service.detail(product_id)

        if not product:
            return "Produto não encontrado." 
        
        if int(product.quantity) > 0:
            return self.render('product_details', product=product)
        
        return self.render('product_details', product=product, status_msg=mensagem_status)
    
       

product_routes = Bottle()
product_controller = ProductController(product_routes)