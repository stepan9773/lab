from flask import request
from flask_login import current_user
from flask_restful import Resource

from app import Ticket
from app import Transaction
from app import db


class BookingByIDRasource(Resource):

    def get(self, id ):
        transaction = Transaction.query.filter_by(id=id, booked=True,user_id=current_user.id).first()
        ticket = Ticket.query.filter_by(id=transaction.ticket_id).first()
        return {
            "id": ticket.id,
            "place": ticket.seat,
            "price": ticket.price,
            "title": ticket.title,
            "date": ticket.date
        }

