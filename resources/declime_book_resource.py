from flask import request

from flask_restful import Resource

from app import Ticket, User
from app import Transaction
from app import db

from flask_jwt_extended import get_jwt_identity, jwt_required
class DeclimeBooking(Resource):
    @jwt_required
    def post(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()

        data = request.get_json()
        ticket_id = data["ticket_id"]
        transaction = Transaction.query.filter_by(id=ticket_id, booked=True, user_id=current_user.id).first()
        if transaction is None:
            return "booking not exist", 404
        ticket = Ticket.query.filter_by(id=transaction.ticket_id).first()

        db.session.delete(transaction)
        db.session.commit()
        db.session.delete(ticket)
        db.session.commit()

        return "Declime dook ", 200
