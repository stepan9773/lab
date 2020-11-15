from flask_restful import Resource
from flask_requests import request
import app


class BookingResource(Resource):

    def get(self):
        my_booking_tickets = []
        for book in app.Booking:
            if book['name'] == app.Curent_user['name']:
                my_booking_tickets.append(book)
        return my_booking_tickets


    def post(self):

        book_ticket = request.get_json()
        for ticket in app.Tickets:
            if ticket['title'] == book_ticket['title'] and ticket['place'] == book_ticket['place']:
                return "this ticked already sold"
        book_transaction = {
            'name': app.Curent_user['name'],
            'title': book_ticket['title'],
            'price': book_ticket['price'],
            'place': book_ticket['place']
        }
        app.Booking.append(book_transaction)
        app.Tickets.append(book_ticket)
        return 'book sucesed', 200




class DeclimeBookingResource(Resource):


    def post(self):
        remuve_ticet = request.get_json()
        for book in app.Booking:
            if book['title'] == remuve_ticet['title'] \
                    and book['place'] == remuve_ticet['place']:
                app.Booking.remove(book)
                for ticket in app.Tickets:
                    if ticket['title'] == remuve_ticet['title'] \
                            and ticket['place'] == remuve_ticet['place']:
                        app.Tickets.remove(ticket)

                return 'Book deleted'
            else:
                return 'this book not in your wallet ', 200