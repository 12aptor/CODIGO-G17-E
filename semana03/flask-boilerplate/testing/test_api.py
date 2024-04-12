import pytest
from app import app
from flask import Flask

jwt = None

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_login(client: Flask):
    response = client.post('/api/auth/login', json = {
        "email": "john@gmail.com",
	    "password": "johnjohn"
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
    token = jwt
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = client.post('/api/products/create', json = {
        "name": "Zapatillas Puma",
        "description": "Zapatillas urbanas de color negro",
        "price": 300.00,
        "stock": 100
    }, headers=headers)

    assert response.status_code == 201
