from flask import request
from flask_login import current_user
from flask_restful import Resource

from app import Ticket
from app import Transaction
from app import db


class BuyRasource(Resource):

    def get(self):
        transactions = Transaction.query.filter_by(user_id=current_user.id,booked=False)
        if transactions is None:
            return "transaction not exist"
        response_dict = {}
        for transaction in transactions:
            response_dict[transaction.id] = {
            "ticket_id": transaction.ticket_id,
            "user_id": transaction.user_id,
            "booked": transaction.booked
        }
        return response_dict


    def post(self):
        if current_user.username == 'user':
            return "tou must loged in firstlly"

        data = request.get_json()
        title = data['title']
        place = data['place']
        date = data['date']
        price = data['price']

        if Ticket.query.filter_by(seat=place, date=date,price=price,title=title).first() is not None:
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
