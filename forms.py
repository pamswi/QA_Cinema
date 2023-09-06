from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired, Length


class DiscussionPost(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    movie_id = IntegerField('Movie ID')
    topic = StringField('Topic', validators=[DataRequired()])
    comment = StringField('Message', validators=[DataRequired()])
    timestamp = DateTimeLocalField('Timestamp', format='%Y-%m-%d %H:%M:%S')
    send = SubmitField('Send')

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