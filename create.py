from application import db, app
from models import User, Movie, Screening, Booking, BookingDetail, Discussion


with app.app_context():
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

    test_movie =  Movie(
            title='Test Movie',
            director='Test Director',
            actors='Actor1, Actor2, Actor3',
            release_date='2023-01-01',
            description='A test movie description',
            poster='movie_poster.jpg',
            classic=True,
            age_restricted=False
        )
    db.session.add(test_movie)
    db.session.commit()

    screening_test = Screening(
            movie_id=1,
            screen_id=1,
            time='2023-01-01 12:00:00',
            current_capacity=100
        )
    db.session.add(screening_test)
    db.session.commit()

    booking_test = Booking(
            user_id=1,
            screening_id=5,
            booking_date='2023-01-01 10:00:00',
            total_price=50,
            discounted_ticket_number=2,
            full_price_ticket_number=3
        )
    db.session.add(booking_test)
    db.session.commit()

    booking_details_test = BookingDetail(
            booking_id=2,
            ticket_type='Adult',
            quantity=2,
            price=50
        )
    db.session.add(booking_details_test)
    db.session.commit()

    discussion_test = Discussion(
            user_id=1,
            movie_id=1,
            topic='Test Topic',
            comment='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non velit sit amet risus condimentum tristique. Sed bibendum elit nec arcu auctor, in malesuada justo tincidunt. Nullam auctor auctor purus, ac dictum ipsum. Vivamus gravida, justo in tristique pulvinar, metus velit blandit metus.',
            timestamp='2023-01-01 14:00:00'
        )
    db.session.add(discussion_test)
    db.session.commit()