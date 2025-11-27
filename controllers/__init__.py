from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.product_controller import product_routes
from controllers.info_controller import info_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(product_routes)
    app.merge(info_routes)