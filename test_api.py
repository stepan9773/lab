from manage import client
from flask import Flask
from flask import jsonify, request
from http import HTTPStatus
from app import db

acces = {}
import pytest


def test_signup():

    data = {
        "username":"test",
        "password":"1234"
    }

    res = client.post("/signup", json=data)
    assert res.status_code == 200

def test_login_OK():
    data = {
        "username": "test",
        "password": "1234"
    }
    res = client.post("/login", json=data)
    acces_token = str(res.get_data())[3:-4]
    acces["token"] = acces_token
    assert res.status_code == 200
    data2 = {
        "username": "te st",
        "password": "12 34"
    }
    res = client.post("/login", json=data2)
    assert res.status_code == 200
    assert int(res.get_data()) == 400
    data3 = {
        "username": "test",
        "password": "12 34"
    }
    res = client.post("/login", json=data3)
    assert res.status_code == 200
    assert int(res.get_data()) == 401


def test_get_smoke():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/smoke", headers=headers)
    assert int(res.get_data())== 200
    assert res.status_code == 200
    res = client.post("/smoke", headers=headers)
    assert res.status_code == 405



"""
def test_manage():

    assert manage.run(Flask("test")) == None
"""

def test_check_pass():
    from resources.login_resource import check_password_hash
    assert check_password_hash("sha256$vBVffk6j$c4fa336a4ba4feaa27f4677c4aa965bd3548a0acb3d6a5be6ddfb081a606d779","string") == True


def test_booking_get():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/book", headers=headers)

    assert res.status_code == 200

