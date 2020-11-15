from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from resources.UserResource import UserResource
from resources.SellersResource import SellersResource
from resources.BookingResource import BookingResource,DeclimeBookingResource
from resources.GetSaticResource import GetStaticResource



SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    },

)

APP_NAME = "Artify"
APP_PREFIX = "/Artif"

Users = []
Tickets = []
Transaction = []
Booking = []

deafoult = {
    'name': 'user',
    'password': '1234',
    'money': 20000
}
Users.append(deafoult)
Curent_user = deafoult




def create_app(config=None):
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """
    app = Flask(APP_NAME)
    api = Api(app)
    app.register_blueprint(swaggerui_blueprint)
    app.config.from_object(config)
    app.logger_name = APP_NAME
    register_buy_ticket_rotes(api)

    register_user_rotes(api)
    register_book_ticket_rotes(api)

    return app

def register_book_ticket_rotes(api):
    api.add_resource(BookingResource, '/book')
    api.add_resource(DeclimeBookingResource, '/decline_book')

def register_buy_ticket_rotes(api):
    api.add_resource(SellersResource, '/buy')

def register_user_rotes(api):
    api.add_resource(UserResource, '/user')

def register_path_rotes(api):
    api.add_resource(GetStaticResource, '/stat/<path:path>')
