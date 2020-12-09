from flask import request
from flask_login import current_user
from flask_restful import Resource

from app import Ticket
from app import Transaction
from app import db


class DeclimeBooking(Resource):

    def post(self):
        data = request.get_json()
        ticket_id = data["transaction_id"]
        transaction = Transaction.query.filter_by(id=ticket_id, booked=True,user_id=current_user.id).first()
        if transaction is None:
            return "booking not exist", 404
        ticket = Ticket.query.filter_by(id=transaction.ticket_id).first()

        db.session.delete(transaction)
        db.session.commit()
        db.session.delete(ticket)
        db.session.commit()


        return "Declime dook ", 200

