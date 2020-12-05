from flask_login import current_user
from flask_restful import Resource

from app import Ticket
from app import Transaction


class BuyByIDRasource(Resource):

    def get(self, id):
        transaction = Transaction.query.filter_by(id=id, booked=False, user_id=current_user.id).first()
        if transaction is None:
            return "transaction not exist"
        ticket = Ticket.query.filter_by(id=transaction.ticket_id).first()
        if ticket is None:
            return "transaction not exist"
        return {
            "id": ticket.id,
            "place": ticket.seat,
            "price": ticket.price,
            "title": ticket.title,
            "date": ticket.date
        }
