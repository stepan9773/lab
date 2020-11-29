from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS

from resources.SendFromDirectorySwagger import SendFromDirectorySwagger
from resources.StudentsUpdateResource import StudentUpdateResources
from resources.StudentsRatingResource import StudentRatingResources
from resources.SmokeResource import SmokeResources
from settings.settings import Config

from flask_sqlalchemy import SQLAlchemy

from flask_swagger_ui import get_swaggerui_blueprint





APP_NAME = "Artify"
APP_PREFIX = "/Artify"

db = SQLAlchemy()




def create_app(config=None):
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """
    app = Flask(APP_NAME)
    api = Api(app, prefix=APP_PREFIX)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///D:/Documents/AppliedProgramming/Lab5/ArtifyAPI/Database/BookingDB.db'

    db.init_app(app)

    # database = db.connect('Database/Institution.db')
    # cursor = database.cursor();
    # cursor.execute('''
    #     Select *
    #     From Students;
    # ''')
    # print(cursor.fetchone())
    app.config.from_object(config)
    app.logger_name = APP_NAME

    register_smoke_rotes(api)
    register_student_update_rotes(api)
    register_student_rating_rotes(api)
    register_send_static_route(api)
    SWAGGER_URL = f'{APP_PREFIX}/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL
        , API_URL
        , config = {
            'app_name' : 'Lab5 API Documentation'
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix = SWAGGER_URL)
    #app.register_blueprint(request_api.get_blueprint())

    return app


def register_smoke_rotes(api):
    """
    Connect to API resource Smoke
    args:
        api: API which connect the resource Smoke
    Returns:
         None
    """
    api.add_resource(SmokeResources, "/smoke")


def register_student_update_rotes(api):
    """
    Connect to API resource StudentUpdate
    args:
        api: API which connect the resource StudentUpdate
    Returns:
         None
    """
    api.add_resource(StudentUpdateResources, "/student_update")


def register_student_rating_rotes(api):
    """
    Connect to API resource StudentRating
    args:
        api: API which connect the resource StudentRating
    Returns:
         None
    """
    api.add_resource(StudentRatingResources, "/student_rating")


def register_send_static_route(api):
    api.add_resource(SendFromDirectorySwagger, "/static/<path:path>")

class Ticket(db.Model):

    ticket_id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.VARCHAR(length=50))
    date = db.Column(db.DATETIME)

    def __init__(self, ticket_id, title, date):
        self.ticket_id = ticket_id
        self.title = title
        self.date = date

class Tickets(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    ticket_id = db.Column(db.INTEGER)
    price = db.Column(db.REAL)
    seat = db.Column(db.INTEGER)

    def __init__(self, id, ticket_id, price, seat):
        self.id = id
        self.ticket_id = ticket_id
        self.price = price
        self.seat = seat


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.INTEGER)
    ticket_id = db.Column(db.INTEGER)
    booked = db.Column(db.BOOLEAN)

    def __init__(self, id, user_id, ticket_id, booked):
        self.id = id
        self.user_id = user_id
        self.ticket_id = ticket_id
        self.booked = booked

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(length=50))
    password = db.Column(db.VARCHAR(length=50))

    def __init__(self, id, username, password, booked):
        self.id = id
        self.username = username
        self.password = password




