from bottle import Bottle
from .base_controller import BaseController
class InfoController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        
        self.setup_routes()
        

    
    
    def setup_routes(self):
        self.app.route('/sahur.info', method='GET', callback=self.info)

    def info(self):
        return self.render('sahur_info')    
    
info_routes = Bottle()
info_controller = InfoController(info_routes)