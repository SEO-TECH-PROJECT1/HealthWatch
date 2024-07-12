import pytest
from HealthWatch.app import app, db, User
from flask import session

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    with app.app_context():
        db.drop_all()

def test_index_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.headers['Location']

def test_register(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'bio': 'Test bio'
    }, follow_redirects=True)
    assert b'User successfully registered!' in response.data

def test_login_logout(client):
    # Register a user
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'bio': 'Test bio'
    })

    # Login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    assert b'Dashboard' in response.data

    # Logout
    response = client.get('/logout', follow_redirects=True)
    assert b'You have been logged out' in response.data

def test_dashboard_access(client):
    # Try accessing dashboard without login
    response = client.get('/dashboard')
    assert response.status_code == 302
    assert '/login' in response.headers['Location']

    # Register and login
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'bio': 'Test bio'
    })
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    })

    # Access dashboard after login
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data