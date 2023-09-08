from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateTimeLocalField,DateField,SelectField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post_id = HiddenField('Post ID')
    username = HiddenField('username')
    topic = StringField('Topic', validators=[DataRequired()])
    content = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    post_id = HiddenField('Post ID')
    content = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

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
    user_id = IntegerField('User ID', validators=[DataRequired()])
    
    Adult = IntegerField('Number of Adult Tickets', default=0)
    Child = IntegerField('Number of Child Tickets', default=0)
    Concession = IntegerField('Number of Concession Tickets', default=0)
    
    submit = SubmitField('Book')


    
