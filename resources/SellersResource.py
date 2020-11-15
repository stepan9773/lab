from flask_restful import Resource
from flask_requests import request
import app


class SellersResource(Resource):
    def get(self):
        my_bought_tickets = []
        for ticket in app.Transaction:
            if ticket['name'] == app.Curent_user['name']:
                my_bought_tickets.append(ticket)
        return my_bought_tickets

    def post(self):
        new_ticet = request.get_json()
        for ticket in app.Tickets:
            if ticket['title'] == new_ticet['title'] and ticket['place'] == new_ticet['place']:
                return 'This ticke already sold'
        if new_ticet['price'] > app.Curent_user['money']:
            return "you don`t have money to buy this ticket "
        else:
            app.Curent_user['money'] -= new_ticet['price']
            transaction = {
                'name': app.Curent_user['name'],
                'title': new_ticet['title'],
                'price': new_ticet['price'],
                'place': new_ticet['place']
            }

            app.Tickets.append(new_ticet)
            app.Transaction.append(transaction)
            return transaction
