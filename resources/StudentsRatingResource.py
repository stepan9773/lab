from flask import jsonify, request
from flask_restful import Resource
from sqlalchemy.ext.automap import automap_base

import app


class StudentRatingResources(Resource):
    """
    GET endpoint to get the list of Students ordered by their rating
    """
    def get(self):
        json = request.get_json()
        desc = json['desc']
        limit = json['limit']
        return jsonify(dict(result=[dict(row) for row in app.db.session.execute(
            f'''
            Select *
            From main.students
            Order by main.students.rating {"DESC" if desc else "ASC"}
            {"" if limit is None else "Limit " f"{int(limit)}"};
            '''
        )]))

    """
    PUT endpoint to update the student's rating
    """
    def put(self):
        json = request.get_json()
        student_id = json['student_id']
        rating = json['rating']
        app.db.session.execute(
            f'''
            Update main.students
            
            Set rating = {rating}
            Where student_id = {student_id};
                
            '''
        )
        app.db.session.commit()
        return "Successful post request are being submitted!", 200
