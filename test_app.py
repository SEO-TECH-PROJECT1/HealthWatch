import unittest
from app import app, db, User

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_and_login(self):
        # Test registration
        response = self.app.post('/register', data=dict(username='testuser', password='testpassword'), follow_redirects=True)
        self.assertIn(b'User successfully registered!', response.data)
        
        # Test login
        response = self.app.post('/login', data=dict(username='testuser', password='testpassword'), follow_redirects=True)
        self.assertIn(b'You should be redirected automatically', response.data)

    def test_dashboard_access(self):
        # Register and login
        self.app.post('/register', data=dict(username='testuser', password='testpassword'), follow_redirects=True)
        self.app.post('/login', data=dict(username='testuser', password='testpassword'), follow_redirects=True)
        
        # Access dashboard
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Dashboard', response.data)

if __name__ == '__main__':
    unittest.main()
