from bottle import Bottle, run
from beaker.middleware import SessionMiddleware
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

    def setup_plugins(self):
        SESSION_OPTS = {
            'session.type': 'memory',
            'session.cookie_expires': True,
            'session.auto': True,
            'session.encrypt_key': self.config.SECRET_KEY,
            'session.validate_key': self.config.SECRET_KEY
        }

        return SESSION_OPTS  

    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)  

    def run(self):
        
        self.setup_routes()

        
        SESSION_OPTS = self.setup_plugins()
        wsgi_app = SessionMiddleware(self.bottle, SESSION_OPTS)

        
        run(
            app=wsgi_app,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER,
            server_options={'reusue_address': True}
        )



def create_app():
    return App()
