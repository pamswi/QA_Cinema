from typing import Any
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateField, SelectField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from filter.swearwords import swearwords


class CheckSwearwords:
    def __init__(self, message=None):
        self.message=message
    def __call__(self, form, field):
        if any(word in field.data.lower().split() for word in swearwords):
            raise ValidationError(self.message)
        
class PostForm(FlaskForm):
    post_id = HiddenField('Post ID')
    username = HiddenField('username')
    movie_id = SelectField('Movie')
    topic = StringField('Topic', validators=[
        DataRequired(), 
        #CheckSwearwords(message='Your topic contains inappropriate language!')
        ])
    content = StringField('Message', validators=[
        DataRequired(),
        #CheckSwearwords(message='Your content contains inappropriate language!')
        ])
    submit = SubmitField('Post')
 
# payment form including Akber's validators
class PayForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(min=4, max=30)])
    last_name = StringField('Last Name', validators=[
        DataRequired(),
        Length(min=2, max=30)]) 
    address = StringField('Address', validators=[
        DataRequired(), 
        Length(min=10, max=200)])
    card_number = StringField('Enter 16 digit Card Number', validators=[
        DataRequired(),
        Length(min=16, max=16)])
    expiry_date = StringField('Enter expiry date MM/YY', validators=[
        DataRequired(),
        Length(min=5, max=5)]) 
    cvc_number = StringField('Enter 3 digit CVC Number', validators=[
        DataRequired(),
        Length(min=3, max=3)])   
    
    submit = SubmitField('Pay Now')


class BookingForm(FlaskForm):  
    Adult = IntegerField('Number of Adult Tickets £15.00', default=0)
    Child = IntegerField('Number of Child Tickets £5.00', default=0)
    Concession = IntegerField('Number of Concession Ticket £10.00 *  ', default=0)
    
    submit = SubmitField('Book')


    
