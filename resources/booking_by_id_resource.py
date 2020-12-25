from flask_login import current_user
from flask_restful import Resource

from app import Ticket,User,Rights
from app import Transaction
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

class BookingByIDRasource(Resource):
    @jwt_required
    def get(self, id):
        transaction = Transaction.query.filter_by(id=id, booked=True, user_id=User.query.filter_by(username=get_jwt_identity()).first().id).first()
        ticket = Ticket.query.filter_by(id=transaction.ticket_id).first()
        if ticket is None:
            return "booking not exist", 404
        return {
            "id": ticket.id,
            "place": ticket.seat,
            "price": ticket.price,
            "title": ticket.title,
            "date": ticket.date
        }
