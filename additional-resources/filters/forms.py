from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateTimeLocalField,DateField,SelectField
from wtforms.validators import DataRequired, Length


class DiscussionPost(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    movie_id = IntegerField('Movie ID')
    topic = StringField('Topic', validators=[DataRequired()])
    comment = StringField('Message', validators=[DataRequired()])
    timestamp = DateTimeLocalField('Timestamp', format='%Y-%m-%d %H:%M:%S')
    send = SubmitField('Send')

class BasicForm(FlaskForm): #Akber form for booking movies
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(min=2, max=30)
    ])
    last_name = StringField('Last Name')
    movie_date = DateField('Movie date')
    num_of_tickets = IntegerField('Number of Seats')
    movie = SelectField('Choose Movie', choices=[
        ('Movie 1', 'Movie 1'),
        ('Movie 2', 'Movie 2'),
        ('Movie 3', 'Movie 3')
    ])
    ticket_type = SelectField('Ticket Type', choices=[
        ('Adult', 'Adult'),
        ('Kids', 'Kids'),
        ('Students', 'Students')
    ])
    username = StringField('Username')
    submit = SubmitField('Add To Order')

    