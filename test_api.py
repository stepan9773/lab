
from flask import Flask
from flask import jsonify, request
from http import HTTPStatus
from app import db,Ticket,User, Transaction,create_app
from manage import client
import manage
import random
import string

acces = {}
import pytest

@pytest.fixture
def user():
    user_data = {
        "username": "test",
        "password": "1234"
    }
    return user_data


@pytest.fixture
def user_not_exist():
    user_not_exist_data = {
        "username": "te st",
        "password": "12 34"
    }
    return user_not_exist_data

@pytest.fixture
def user_frong_pass():
    user_data = {
        "username": "test",
        "password": "12 34"
    }
    return user_data


def test_signup(user):
    res = client.post("/signup", json=user)
    assert res.status_code == 200

def test_login_not_OK(user,user_frong_pass,user_not_exist):

    res = client.post("/login", json=user)
    acces_token = str(res.get_data())[3:-4]
    acces["token"] = acces_token
    assert res.status_code == 200

    res = client.post("/login", json=user_not_exist)
    assert res.status_code == 200
    assert int(res.get_data()) == 400

    res = client.post("/login", json=user_frong_pass)
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



def test_check_pass():
    from resources.login_resource import check_password_hash
    assert check_password_hash("sha256$vBVffk6j$c4fa336a4ba4feaa27f4677c4aa965bd3548a0acb3d6a5be6ddfb081a606d779","string") == True


def test_booking_get():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/book", headers=headers)

    assert res.status_code == 200
    assert res.get_data() is not None

@pytest.fixture
def ticket():
    place = random.randint(0,256)
    price = random.randint(110,11256)
    ticket= {

        'title':"test",
        'place':place,
        'date':"",
        'price':price
    }
    return ticket
def test_booking_post(ticket):
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }

    res = client.post("/book", headers=headers, json=ticket)

    assert res.status_code == 200
    assert res.get_data() is not None


@pytest.fixture
def execute_ticket():

    tick = {
        'title': "test",
        'place': 58,
        'date': "",
        'price': 11142
    }
    return tick

def test_booking_post_exist(execute_ticket):
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }

    res = client.post("/book", headers=headers, json=execute_ticket)

    assert res.status_code == 404
    assert res.get_data() is not None


def test_book_get_by_id():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/book/20", headers=headers)

    assert res.status_code == 200
    assert res.get_data() is not None

def test_ticket_by_id():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/buy/1000", headers=headers)
    assert res.status_code == 404
def test_ticket_by_id2():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/buy/27", headers=headers)
    assert res.status_code == 200

def test_buy_get():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/buy", headers=headers)
    assert res.status_code == 200
    assert res.get_data() is not None
def test_buy_post_exist(execute_ticket):
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }

    res = client.post("/buy", headers=headers, json=execute_ticket)

    assert res.status_code == 404
    assert res.get_data() is not None

def test_buy_post(ticket):
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }

    res = client.post("/buy", headers=headers, json=ticket)

    assert res.status_code == 200
    assert res.get_data() is not None


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

@pytest.fixture
def goo_user():
    user_data = {
        "username": str(get_random_string(8)),
        "password":  str(get_random_string(8))
    }
    return user_data

def test_good_signup(goo_user):
    res = client.post("/signup", json=goo_user)
    assert res.status_code == 200


def test_user_get():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/user", headers=headers)
    assert res.status_code == 200
    assert res.get_data() is not None


def test_user_id_get():
    headers = {
        'Authorization': 'Bearer {}'.format(acces["token"])
    }
    res = client.get("/user/15", headers=headers)
    assert res.status_code == 200
    assert res.get_data() is not None

@pytest.fixture
def create_app_test():
    app = create_app()
    return app

def test_app(create_app_test):
    assert create_app_test is not None

def test_manege():
    assert manage.client is not None

