from flask_restful import Resource
import jsonify
from flask_requests import request
import app
import jsonify


class UserResource(Resource):

    def get(self):
        print(app.Curent_user)
        my_tickets = []
        for ticket in app.Transaction:
            if app.Curent_user['name'] == ticket['name']:
                my_tickets.append(ticket)

        return dict(app.Curent_user)


    def post(self):
        data = request.get_json()
        new_user = {
            'name': data['name'],
            'password': data['password'],
            'money': data['money']
        }

        for user in app.Users:
            if user['name'] == new_user['name'] and user['password'] == new_user['password']:
                app.Curent_user = new_user
                return 200
            return "NO users with current name ad password"


    def put(self):
        data = request.get_json()
        new_user = {
            'name': data['name'],
            'password': data['password'],
            'money': data['money']
        }
        app.Users.append(new_user)
        app.Curent_user = new_user
        return 200


    def delete(self):
        app.Users.remove(app.Curent_user)
        app.Curent_user = app.deafoult
        return 200
