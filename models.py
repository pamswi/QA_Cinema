from application import db, app
from flask import session

'''
once the connection to the database is established, the following file creates tables
'''
class Screen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seating_capacity = db.Column(db.Integer, default=231)

    # screenings = db.relationship('Screening', backref='screen')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    address = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    card_number = db.Column(db.String(16))
    card_expiry = db.Column(db.String(7)) 
    card_cvc = db.Column(db.Integer)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    director = db.Column(db.String(255))
    actors = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    classic = db.Column(db.Boolean)
    age_restricted = db.Column(db.Boolean)

class Screening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
    screen_id = db.Column('screen_id', db.String(5), db.ForeignKey('screen.id'))
    time = db.Column(db.DateTime)
    current_capacity = db.Column(db.Integer)

    movie = db.relationship('Movie', backref='screening')
    screen = db.relationship('Screen', backref='screening')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    screening_id = db.Column('screening_id', db.Integer, db.ForeignKey('screening.id'))
    booking_date = db.Column(db.DateTime)
    total_price = db.Column(db.Integer)
    discounted_ticket_number = db.Column(db.Integer)
    full_price_ticket_number = db.Column(db.Integer)

    user = db.relationship('User', backref='booking')
    screening = db.relationship('Screening', backref='booking')

class BookingDetal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column('booking_id', db.Integer, db.ForeignKey('booking.id'))
    ticket_type = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    booking = db.relationship('Booking', backref='detail')


class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
    topic = db.Column(db.String(255))
    comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)

    user = db.relationship('User', backref='discussion')
    movie = db.relationship('Movie', backref='discussion')
