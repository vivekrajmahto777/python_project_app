#test_app.py

import pytest
from app import create_app
from urllib.parse import quote_plus

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = 'Hello geeks how are you this is my flask server'
    assert expected_text.encode() in response.data
