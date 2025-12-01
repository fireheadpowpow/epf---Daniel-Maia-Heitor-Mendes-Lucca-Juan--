from bottle import Bottle, request
from .base_controller import BaseController
from services.login_services import LoginService
class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        
        self.login_service = LoginService()
        self.setup_routes()
        
        
    def setup_routes(self):
        self.app.route('/sahur.login', method=['GET', 'POST'], callback=self.login)

    def login(self):
        session = request.environ['beaker.session']
        if session.get('autenticado'):
            return self.redirect('/sahurhomepage')
    
        if request.method == 'POST':
            chave_digitada = request.forms.get('secret_key')
            
            autenticado = self.login_service.secret_key(chave_digitada) 

            if autenticado:
            
                session['autenticado'] = True
                
                
                return self.redirect('/sahurhomepage') 
            else:
                
            
                return self.render('secret_key')

        return self.render('secret_key')
    
login_routes = Bottle()
login_controller = LoginController(login_routes)