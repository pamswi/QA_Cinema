from application import db, app
from flask import session
from datetime import datetime

'''
once the connection to the database is established, the following file creates tables and their methods
'''
class Screen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    standard = db.Column(db.Boolean)
    seating_capacity = db.Column(db.Integer, default=231)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    card_number = db.Column(db.String(16))
    card_expiry = db.Column(db.String(7)) 
    card_cvc = db.Column(db.Integer)

    # create a query that filters the users table and checks for username uniqueness
    # the method returns "True" when the username is unique
    @classmethod
    def check_unique_username(cls, username):
        existing_user = cls.query.filter_by(username=username).first()
        return existing_user is None
    
    @classmethod
    def retrieve_user(cls, username):
        existing_user = cls.query.filter_by(username=username).first()
        return existing_user
   
    @classmethod
    def add_payment(cls, username, first_name, last_name, address, card_number, card_expiry, card_cvc):
        user = cls.query.filter_by(username=username).first()
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.address = address
            user.card_number = card_number
            user.card_expiry = card_expiry
            user.card_cvc = card_cvc
            db.session.add(user)
            db.session.commit()
            return user
        else:
            return "user not found"
        

    @classmethod
    def add_user(cls, username, email, password):
        new_user=User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    director = db.Column(db.String(255))
    actors = db.Column(db.Text)
    release_date = db.Column(db.String(255))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    classic = db.Column(db.Boolean)
    age_restricted = db.Column(db.Boolean)

    @classmethod
    def movie_by_id(cls, movie_id):
        return cls.query.get(movie_id)
    
    @classmethod
    def all_movies(cls):
        return cls.query.all()
    
    @classmethod
    def get_classic_movies(cls):
        return cls.query.filter_by(classic=True).all()
    
    @classmethod
    def get_current_movies(cls):
        return cls.query.filter_by(classic=False).all()
    
    # the following method retrievs movies similar to user's search input
    @classmethod
    def search(cls, user_input):
        results = cls.query.filter(cls.title.ilike(f"%{user_input}%")).all()
        return results

class Screening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
    screen_id = db.Column('screen_id', db.Integer, db.ForeignKey('screen.id'))
    time = db.Column(db.String(50))
    day = db.Column(db.String(50))
    current_capacity = db.Column(db.Integer)

    movie = db.relationship('Movie', backref='screening')
    screen = db.relationship('Screen', backref='screening')

    @classmethod
    def screenings_by_movie(cls, movie_id):
        return cls.query.get(movie_id)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    screening_id = db.Column('screening_id', db.Integer, db.ForeignKey('screening.id'))
    booking_date = db.Column(db.Date, nullable=False, default=datetime.now)
    total_price = db.Column(db.Integer)

    user = db.relationship('User', backref='booking')
    screening = db.relationship('Screening', backref='booking')

    @classmethod
    def book_movie(cls, user_id, screening_id, total_price):
        new_booking = cls(
            user_id=user_id,
            screening_id=screening_id,
            total_price=total_price
        )    
        db.session.add(new_booking)
        db.session.commit()
        return new_booking

    @classmethod
    def booking_by_id(cls, booking_id):
        return cls.query.get(booking_id)
    
    @classmethod
    def bookings_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

class BookingDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column('booking_id', db.Integer, db.ForeignKey('booking.id'))
    ticket_type = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    booking = db.relationship('Booking', backref='details')

    @classmethod
    def add_booking_detail(cls, booking_id, ticket_type, quantity, price):
        detail = cls(
            booking_id=booking_id,
            ticket_type=ticket_type,
            quantity=quantity,
            price=price
        )
        db.session.add(detail)
        db.session.commit()
        return detail

    @classmethod
    def details_by_booking(cls, booking_id):
        return cls.query.filter_by(booking_id=booking_id).all()

    


class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), db.ForeignKey('user.username'))
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
    topic = db.Column(db.String(255))
    responding_to = db.Column(db.String(20))
    content = db.Column(db.String(500))
    timestamp = db.Column(db.String(20))

    user = db.relationship('User', primaryjoin='Discussion.username == User.username',backref='discussion')
    movie = db.relationship('Movie', primaryjoin='Discussion.movie_id == Movie.id',backref='discussion')

    @classmethod
    def all_discussion(cls):
        return cls.query.all()
    
    @classmethod
    def all_posts(cls):
        return cls.query.filter(cls.responding_to == "Post").all()
    
    @classmethod
    def all_comments(cls):
        # return cls.query.filter(cls.responding_to != "Post").all()
        return cls.query.filter(cls.responding_to != "Post").all()
    
    @classmethod
    def new_post(self, username, movie_id, topic, responding_to, content, timestamp):
        new_post=Discussion(username=username, movie_id=movie_id, topic=topic, responding_to=responding_to, content=content, timestamp=timestamp)
        db.session.add(new_post)
        db.session.commit()
        return new_post