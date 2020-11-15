from flask_restful import Resource
from flask import  send_from_directory

class GetStaticResource(Resource):
    def get(self, path):
        return send_from_directory('static/', path)
