from flask import Flask
from flask_restful import Api

from flask_login import  UserMixin

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import request,jsonify

from flask_swagger_ui import get_swaggerui_blueprint


db = SQLAlchemy()
migrate = Migrate()




def create_app(config=None):
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """
    app = Flask(__name__)
    api = Api(app)



    jwt = JWTManager(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:1234@localhost:5432/booking_db'
    app.config['SECRET_KEY'] = 'stepan'
    app.config.from_object(config)
    app.logger_name = __name__
    db.init_app(app)
    migrate.init_app(app, db)

    register_smoke_rotes(api)




    import_bluprint_resource()

    SWAGGER_URL = f'/swagger'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL
        , API_URL
        , config={
            'app_name': 'Lab7 API Documentation'
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app


class Ticket(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.VARCHAR(length=50))
    date = db.Column(db.String(50))
    price = db.Column(db.REAL)
    seat = db.Column(db.INTEGER)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey("user.id"))
    ticket_id = db.Column(db.INTEGER, db.ForeignKey("ticket.id"))
    booked = db.Column(db.BOOLEAN)



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(length=50), unique=True)
    password = db.Column(db.VARCHAR(length=256))

class Rights(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey("user.id"))
    admin = db.Column(db.Boolean)


from resources.user_by_id_resource import UserByIDRasource
from resources.booking_resource import BookingRasource
from resources.booking_by_id_resource import BookingByIDRasource
from resources.declime_book_resource import DeclimeBooking
from resources.buy_by_id_resource import BuyByIDRasource
from resources.buy_resource import BuyRasource
from resources.user_resource import UserRasource
from resources.login_resource import LoginResource
from resources.signup_resource import SignupResource
from resources.administrator_resource import AdminResource
from resources.SmokeResource import SmokeResources
def register_smoke_rotes(api):
    """
    Connect to API resource Smoke
    args:
        api: API which connect the resource Smoke
    Returns:
         None
    """
    api.add_resource(SmokeResources, "/smoke")
    api.add_resource(UserByIDRasource, "/user/<int:id>")
    api.add_resource(BookingRasource, "/book")
    api.add_resource(BookingByIDRasource, "/book/<int:id>")
    api.add_resource(DeclimeBooking, '/decline_book')
    api.add_resource(BuyRasource, '/buy')
    api.add_resource(BuyByIDRasource, '/buy/<int:id>')
    api.add_resource(UserRasource, '/user')
    api.add_resource(LoginResource, '/login')
    api.add_resource(SignupResource, '/signup')
    api.add_resource(AdminResource, '/admin')
def import_bluprint_resource():


    pass