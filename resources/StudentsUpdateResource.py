from flask import jsonify, request
from flask_restful import Resource
from sqlalchemy.ext.automap import automap_base

import app


class StudentUpdateResources(Resource):
    """
    GET endpoint to get single student info
    """
    def get(self):
        json = request.get_json()
        student_id = json['student_id']
        return jsonify(dict(result=[dict(row) for row in app.db.session.execute(
            f'''
            Select *
            From main.students
            Where main.students.student_id == {student_id};
            '''
        )])), 200

    """
    PUT endpoint to update the database, by removing the student by its id
    """
    def put(self):
        json = request.get_json()
        student_id = json['student_id']
        app.db.session.execute(
            f'''
            Delete
            From main.students
            Where student_id = {student_id};
            '''
        )
        return f"Student {student_id} was successfully removed from DB", 200

    """
    POST endpoint to add new students to database 
    n - number of students to be added as nested JSON
    """
    def post(self):
        json = request.get_json()
        students_total = json['n']
        for n in range(students_total):
            stud = app.Students(
                rating = json['students'][n]['rating']
                , first_name = json['students'][n]['first_name']
                , last_name = json['students'][n]['last_name']
                , description = json['students'][n]['description']
            )
            app.db.session.add(stud)
            app.db.session.commit()
        return "Successful post request are being submitted!", 200
        # return jsonify(json_list = app.db.session.execute('''
        #     Select *
        #     From main.students
        # '''))
        # return app.db.session.execute('''
        #     Select *
        #     From main.students
        # ''').fetchall()
