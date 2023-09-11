import pytest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from models import User, Screen, Movie, Screening, Discussion, Booking
import os

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            #SQLALCHEMY_DATABASE_URI = 'sqlite:///testdata.db',
            SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI"),
            #export DATABASE_URI=mysql+pymysql://root:pass@localhost/test_qa_cinema
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
    
    def setUp(self):
        db.drop_all()
        db.create_all()

        test_user = User(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            address='123 Test St',
            first_name='Test',
            last_name='User',
            card_number='1234567890123456',
            card_expiry='12/24',
            card_cvc=123
        )
        db.session.add(test_user)
        db.session.commit()

        test_movies =  [
            Movie(title='Test Movie', director='Test Director', actors='Actor1, Actor2, Actor3', release_date='2023-01-01', description='A test movie description', poster='movie_poster.jpg', classic=True, age_restricted=False),
            Movie(title='Test Movie2', director='Test Director', actors='Actor1, Actor2, Actor3', release_date='2023-01-01', description='A test movie description', poster='movie_poster2.jpg', classic=False, age_restricted=True)
        ]
        db.session.add_all(test_movies)
        db.session.commit()

        test_screens = [
            Screen(standard=True),
            Screen(standard=False, seating_capacity=59)
        ]
        db.session.add_all(test_screens)
        db.session.commit()

        test_screenings = [
            Screening(movie_id=1, screen_id=1, time='12:00:00', day ='Friday', current_capacity=100),
            Screening(movie_id=2, screen_id=2, time='12:00:00', day ='Friday', current_capacity=25)
        ]  
        db.session.add_all(test_screenings)
        db.session.commit()

        test_discussions = [
            Discussion(username=test_user.username, movie_id=test_movies[0], topic="Test Topic 1", responding_to="Post", content="Test content for Test Topic 1", timestamp="01/01/2023 12:00"),
            Discussion(username=test_user.username, movie=test_movies[1], topic="Test Topic 2", responding_to="Post", content="Test content for Test Topic 2", timestamp="01/01/2023 12:30"),
            Discussion(username=test_user.username, movie=test_movies[0], topic="Test Topic 1", responding_to=1, content="Test comment for Test Topic 1", timestamp="01/01/2023 13:00"),
        ]
        db.session.add_all(test_discussions)
        db.session.commit()

        # booking_test = Booking(
        #         user_id=1,
        #         screening_id=5,
        #         booking_date='2023-01-01 10:00:00',
        #         total_price=50,
        #         discounted_ticket_number=2,
        #         full_price_ticket_number=3
        #     )
        # db.session.add(booking_test)
        # db.session.commit()

        # booking_details_test = BookingDetail(
        #         booking_id=2,
        #         ticket_type='Adult',
        #         quantity=2,
        #         price=50
        #     )
        # db.session.add(booking_details_test)
        # db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
   
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_opening_times_get(self):
        response = self.client.get(url_for('opening_times'))
        self.assertEqual(response.status_code, 200)
    
    def test_classifications_get(self):
        response = self.client.get(url_for('classifications'))
        self.assertEqual(response.status_code, 200)

    def test_screens_get(self):
        response = self.client.get(url_for('screens'))
        self.assertEqual(response.status_code, 200)

    def test_cinema_services_get(self):
        response = self.client.get(url_for('cinema_services'))
        self.assertEqual(response.status_code, 200)

    def test_view_movie_get(self):
        response = self.client.get(url_for('view_movie', movie_id=1))
        self.assertEqual(response.status_code, 200)

    def test_api_view_screenings_get(self):
        response = self.client.get(url_for('api_view_screenings', movie_id=1))
        self.assertEqual(response.status_code, 200)

    def test_listings_get(self):
        response = self.client.get(url_for('listings'))
        self.assertEqual(response.status_code, 200)

    def test_new_releases_get(self):
        response = self.client.get(url_for('new_releases'))
        self.assertEqual(response.status_code, 200)

    def test_classics_get(self):
        response = self.client.get(url_for('classics'))
        self.assertEqual(response.status_code, 200)

    def test_search_results_get(self):
        response = self.client.get(url_for('search_results'))
        self.assertEqual(response.status_code, 200)

    def test_payment_get(self):
        response = self.client.get(url_for('payment', screening_id=1))
        self.assertEqual(response.status_code, 200)

    def test_signup_get(self):
        response = self.client.get(url_for('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_get(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 200)

    # Forum
    def test_forum_get(self):
        response = self.client.get(url_for('forum'))
        self.assertEqual(response.status_code, 200)

    def test_forum_post(self):
        response = self.client.post(
            url_for('forum'),
            data = {
                "username": 'testuser', 
                "responding_to": "Post",
                "movie_id": 1,
                "topic": "Test Topic 3",
                responding_to="Post", content="Test content for Test Topic 1", timestamp="01/01/2023 12:00")
            }
        )

    # def test_booking_get(self):
    #     # Replace <screening_id> with an actual screening_id to test the route
    #     response = self.client.get(url_for('book_movie', screening_id=<screening_id>))
    #     self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')