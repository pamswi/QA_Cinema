import pytest
from flask import url_for, Flask
from flask_testing import TestCase
from application import app, db
from models import User, Discussion, Movie, Screening, Booking, BookingDetail
import os

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv("TESTDB_URI"),
            WTF_CSRF_ENABLED=False
        )
        return app
        
    def setUp(self):
        db.create_all()

        user = User(
            username='testuser123',
            email='test@example.com',
            password='password123',
            first_name='John',
            last_name='Doe',
            address='123 Main St',
            card_number='1234567890123456',
            card_expiry='12/25',
            card_cvc=123
            )
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_search_post(self):
        response = self.client.post(url_for('search_results'), data={'searchinput': 'the'})
    
        assert response.status_code == 200
        assert b'new_releases.html' in response.data
        assert b'films' in response.data
        assert b'Gone with the Wind' in response.data
        assert b'The Godfather' in response.data
        assert b'The Wizard of Oz' in response.data
        assert b'The Nun II' in response.data