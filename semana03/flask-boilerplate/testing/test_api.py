import pytest
from app import app
from flask import Flask

jwt = None
user_email = None
user_password = None

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_signup(client: Flask):
    json = {
        "name": "John Doe",
        "document_type": "DNI",
        "document_number": "87654321",
        "email": "john@gmail.com",
        "password": "johnjohn",
        "status": False
    }
    response = client.post('/api/auth/signup', json=json)

    assert response.status_code == 201
    global user_email
    global user_password
    user_email = json['email']
    user_password = json['password']

def test_login(client: Flask):
    response = client.post('/api/auth/login', json = {
        "email": user_email,
	    "password": user_password
    })

    assert response.status_code == 200
    assert 'access_token' in response.json
    assert 'refresh_token' in response.json
    global jwt
    jwt = response.json['access_token']

def test_products_get(client: Flask):
    response = client.get('/api/products/all')
    assert response.status_code == 200
    assert type(response.json) == list

def test_products_post(client: Flask):
    headers = {
        'Authorization': f'Bearer {jwt}'
    }
    response = client.post('/api/products/create', json = {
        "name": "Zapatillas Puma",
        "description": "Zapatillas urbanas de color negro",
        "price": 300.00,
        "stock": 100
    }, headers=headers)

    assert response.status_code == 201
