from application import db, app
from models import User, Movie, Screening, Booking, BookingDetail, Discussion


with app.app_context():
    db.drop_all()
    db.create_all()

    classic_movies = [
    Movie(title="Casablanca", director="Michael Curtiz", actors="Humphrey Bogart, Ingrid Bergman", release_date="1942-01-23", description="A classic romance set during World War II.", poster="casablanca.jpg", classic=True, age_restricted=False),
    Movie(title="Gone with the Wind", director="Victor Fleming", actors="Clark Gable, Vivien Leigh", release_date="1939-12-15", description="An epic historical drama.", poster="gonewiththewind.jpg", classic=True, age_restricted=False),
    Movie(title="The Godfather", director="Francis Ford Coppola", actors="Marlon Brando, Al Pacino", release_date="1972-03-24", description="A crime drama masterpiece.", poster="thegodfather.jpg", classic=True, age_restricted=False),
    Movie(title="Citizen Kane", director="Orson Welles", actors="Orson Welles, Joseph Cotten", release_date="1941-09-05", description="A groundbreaking drama film.", poster="citizenkane.jpg", classic=True, age_restricted=False),
    Movie(title="Schindler's List", director="Steven Spielberg", actors="Liam Neeson, Ralph Fiennes", release_date="1993-12-15", description="A powerful Holocaust drama.", poster="schindlerslist.jpg", classic=True, age_restricted=False),
    Movie(title="Lawrence of Arabia", director="David Lean", actors="Peter O'Toole, Alec Guinness", release_date="1962-12-10", description="An epic adventure in the Arabian desert.", poster="lawrenceofarabia.jpg", classic=True, age_restricted=False),
    Movie(title="The Wizard of Oz", director="Victor Fleming", actors="Judy Garland, Frank Morgan", release_date="1939-08-15", description="A beloved family fantasy film.", poster="wizardofoz.jpg", classic=True, age_restricted=False),
    Movie(title="The Shawshank Redemption", director="Frank Darabont", actors="Tim Robbins, Morgan Freeman", release_date="1994-09-10", description="A tale of hope and friendship in prison.", poster="shawshankredemption.jpg", classic=True, age_restricted=False),
]
    db.session.add_all(classic_movies)
    db.session.commit()



    # test_user = User(
    #         username='testuser',
    #         email='testuser@example.com',
    #         password='password123',
    #         address='123 Test St',
    #         first_name='Test',
    #         last_name='User',
    #         card_number='1234567890123456',
    #         card_expiry='12/24',
    #         card_cvc=123
    #     )
    # db.session.add(test_user)
    # db.session.commit()

    # test_movie =  Movie(
    #         title='Test Movie',
    #         director='Test Director',
    #         actors='Actor1, Actor2, Actor3',
    #         release_date='2023-01-01',
    #         description='A test movie description',
    #         poster='movie_poster.jpg',
    #         classic=True,
    #         age_restricted=False
    #     )
    # db.session.add(test_movie)
    # db.session.commit()

    # screening_test = Screening(
    #         movie_id=1,
    #         screen_id=1,
    #         time='2023-01-01 12:00:00',
    #         current_capacity=100
    #     )
    # db.session.add(screening_test)
    # db.session.commit()

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

    # discussion_test = Discussion(
    #         user_id=4,
    #         movie_id=6,
    #         topic='Discussion Topic',
    #         comment='A test comment',
    #         timestamp='2023-01-01 14:00:00'
    #     )
    # db.session.add(discussion_test)
    # db.session.commit()