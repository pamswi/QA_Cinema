from application import db, app
from models import User, Movie, Screening, Booking, BookingDetail, Discussion, Screen


with app.app_context():
    db.drop_all()
    db.create_all()

    movies = [
    Movie(title="Casablanca", director="Michael Curtiz", actors="Humphrey Bogart, Ingrid Bergman", release_date="1942-01-23", description="A classic romance set during World War II.", poster="casablanca.jpg", classic=True, age_restricted=False),
    Movie(title="Gone with the Wind", director="Victor Fleming", actors="Clark Gable, Vivien Leigh", release_date="1939-12-15", description="An epic historical drama.", poster="gonewiththewind.jpg", classic=True, age_restricted=False),
    Movie(title="The Godfather", director="Francis Ford Coppola", actors="Marlon Brando, James Caan, Al Pacino, Robert Duvall", release_date="24 March 1972", description="The Godfather \"Don\" Vito Corleone is the head of the Corleone mafia family in New York. He is at the event of his daughter's wedding. Michael, Vito's youngest son and a decorated WW II Marine is also present at the wedding. Michael seems to be uninterested in being a part of the family business.", poster="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", classic=True, age_restricted=True),
    Movie(title="Citizen Kane", director="Orson Welles", actors="Orson Welles, Joseph Cotten", release_date="1941-09-05", description="A groundbreaking drama film.", poster="citizenkane.jpg", classic=True, age_restricted=False),
    Movie(title="Schindler's List", director="Steven Spielberg", actors="Liam Neeson, Ralph Fiennes", release_date="1993-12-15", description="A powerful Holocaust drama.", poster="schindlerslist.jpg", classic=True, age_restricted=False),
    Movie(title="Lawrence of Arabia", director="David Lean", actors="Peter O'Toole, Alec Guinness", release_date="1962-12-10", description="An epic adventure in the Arabian desert.", poster="lawrenceofarabia.jpg", classic=True, age_restricted=False),
    Movie(title="The Wizard of Oz", director="Victor Fleming", actors="Judy Garland, Frank Morgan", release_date="1939-08-15", description="A beloved family fantasy film.", poster="wizardofoz.jpg", classic=True, age_restricted=False),
    Movie(title="Scrapper", director="Charlotte Regan", actors="Harris Dickinson, Lola Campbell, Alin Uzun", release_date="25 August 2023", description="In this vibrant and inventive father-daughter comedy, Georgie (Lola Campbell) is a dreamy 12-year-old girl who lives alone in her London flat, filling it with magic after the death of her mother. Out of nowhere, her estranged father Jason (Harris Dickinson) arrives and forces her to confront reality. Uninterested in this sudden new parental figure, Georgie is stubbornly resistant to his efforts. As they adjust to their new circumstances, Georgie and Jason find that both father and daughter still have a lot of growing up to do.", poster="https://s3.amazonaws.com/nightjarprod/content/uploads/sites/130/2023/06/30190749/czuHcf5d45tEgTHjWGkwB9NhbLO.jpg", classic=False, age_restricted=False),
    Movie(title="Oppenheimer", director="Christopher Nolan", actors="Cillian Murphy, Robert Downey Jr, Emily Blunt", release_date="21 July 2023", description="Written and directed by Christopher Nolan and produced by Emma Thomas, Atlas Entertainment's Charles Roven and Nolan, 'Oppenheimer' stars Cillian Murphy (Inception, The Dark Knight trilogy, A Quiet Place Part II, Peaky Blinders) as J. Robert Oppenheimer. 'Oppenheimer' is based on the Pulitzer Prize-winning book American Prometheus: The Triumph and Tragedy of J. Robert Oppenheimer", poster="https://movies.universalpictures.com/media/opr-tsr1sheet3-look2-rgb-3-1-1-64545c0d15f1e-1.jpg", classic=False, age_restricted=False),
    Movie(title="Barbie", director="Greta Gerwig", actors="Margot Robbie, Ryan Gosling", release_date="21 July 2023", description="Eccentric and individualistic, Barbie is exiled from Barbieland because of her imperfections. When her home world is in peril, Barbie returns with the knowledge that what makes her different also makes her stronger.", poster="https://i.ebayimg.com/images/g/gBQAAOSwADJkLV20/s-l1600.jpg", classic=False, age_restricted=False),
    Movie(title="Elemental", director="Peter Sohn", actors="Leah Lewis, Catherine O'Hara, Mamoudou Athie", release_date="7th July 2023", description="In a city where fire, water, land, and air residents live together, a fiery young woman and a go-with-the-flow guy are about to discover something elemental: How much they actually have in common.", poster="https://i0.wp.com/pixarpost.com/wp-content/uploads/2023/06/Elemental-Fandango-Character-Poster.jpg?fit=1080%2C1600&ssl=1", classic=False, age_restricted=False),
    Movie(title="The Nun II", director="Michael Chaves", actors="Storm Reid, Jonas Bloquet, Taissa Farmiga", release_date="8th September 2023", description="1956 - France. A priest is murdered. An evil is spreading. The sequel to the worldwide smash hit follows Sister Irene as she once again comes face-to-face with Valak, the demon nun.", poster="https://s.yimg.com/ny/api/res/1.2/E3Cj4_sKrdgI4zjmWxW7kA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTE2NTY7aD0yMDQ0/https://media.zenfs.com/en/comingsoon_net_477/c817943ce8ab06c0275d03ff03a6dd19", classic=False, age_restricted=False),
    Movie(title="Jurassic Park", director="Steven Spielberg", actors="Sam Neill, Laura Dern, Jeff Goldblum", release_date="1st September 2023", description="During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.", poster="https://m.media-amazon.com/images/I/610fuvWAaqL._AC_UF894,1000_QL80_.jpg", classic=True, age_restricted=False)
    ]


    db.session.add_all(movies)
    db.session.commit()

    screens = [
    Screen(standard=True),
    Screen(standard=True),
    Screen(standard=True),
    Screen(standard=True),
    Screen(standard=True),
    Screen(standard=False, seating_capacity=59),
    Screen(standard=False, seating_capacity=59),
    ]

    db.session.add_all(screens)
    db.session.commit()

    screening_times = [
    '15:00','18:00','21:00',
    ]
    screening_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selected_movies = movies[:7]
    all_screening_times = []

    for _ in range(3):
        all_screening_times.extend(screening_times)

    for day in screening_days:
        for i, movie in enumerate(selected_movies):
            screen = screens[i % len(screens)]
            
            time_indices = [i % len(all_screening_times) for i in range(3)]
            times = [all_screening_times[index] for index in time_indices]

            current_capacity = screen.seating_capacity

            for time in times:
                screening = Screening(
                    movie=movie,
                    screen=screen,
                    time=time,
                    day=day,
                    current_capacity=current_capacity
                )
                db.session.add(screening)

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

    screening_test = Screening(
        movie_id=14,
        screen_id=1,
        time='12:00:00',
        day ='Friday',
        current_capacity=100
    )
         
    db.session.add(screening_test)
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

    discussion_test = Discussion(
            user_id=1,
            movie_id=1,
            topic='Test Topic',
            content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non velit sit amet risus condimentum tristique. Sed bibendum elit nec arcu auctor, in malesuada justo tincidunt. Nullam auctor auctor purus, ac dictum ipsum. Vivamus gravida, justo in tristique pulvinar, metus velit blandit metus.',
            timestamp='2023-01-01 14:00:00'
    )
    db.session.add(discussion_test)
    db.session.commit()