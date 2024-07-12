import pytest
from app import app, db, User

@pytest.fixture
def test_user():
    user = User(username='testuser', email='test@example.com')
    user.set_password('testpassword')
    return user

def test_user_creation(test_user):
    assert test_user.username == 'testuser'
    assert test_user.email == 'test@example.com'
    assert test_user.check_password('testpassword')

def test_user_password_hashing(test_user):
    assert test_user.password_hash != 'testpassword'
    assert test_user.check_password('testpassword')
    assert not test_user.check_password('wrongpassword')

def test_user_representation(test_user):
    assert repr(test_user) == '<User testuser>'