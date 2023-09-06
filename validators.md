To use the form validators
import the following:
from wtforms.validators import ValidationError, DataRequired, Length

example code 
class PayForm(FlaskForm):
    card_num = StringField('Enter 16 digit Card Number', validators=[
        DataRequired(),
        Length(min=16, max=16)])

DataRequired and lenths are the validators in this code

This will not let the user submit if form is empty or char is less than 16 or more than 16.
