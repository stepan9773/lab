from flask import request

from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app import Ticket , User,Rights
from app import Transaction
from app import db


class BuyRasource(Resource):
    @jwt_required
    def get(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()

        transactions = Transaction.query.filter_by(user_id=current_user.id, booked=False)

        response_dict = {}
        for transaction in transactions:
            response_dict[transaction.id] = {
                "ticket_id": transaction.ticket_id,
                "user_id": transaction.user_id,
                "booked": transaction.booked
            }
        return response_dict

    @jwt_required
    def post(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()

        data = request.get_json()
        title = data['title']
        place = data['place']
        date = data['date']
        price = data['price']

        if Ticket.query.filter_by(seat=place, date=date, price=price, title=title).first() is not None:
            return "this ticked are sold", 404

        ticket = Ticket(seat=place, date=date, price=price, title=title)
        db.session.add(ticket)
        db.session.commit()
        transaction = Transaction(
            ticket_id=Ticket.query.filter_by(
                seat=place,
                date=date,
                price=price,
                title=title).first().id,
            user_id=current_user.id,
            booked=False)

        db.session.add(transaction)
        db.session.commit()
        return {
            "id": transaction.id,
            "ticket_id": transaction.ticket_id,
            "user_id": transaction.user_id,
            "booked": transaction.booked
        }
