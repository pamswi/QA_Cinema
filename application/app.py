from typing import Any
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
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
        ('Studetns', 'Students')
    ])
    username = StringField('Username')
    submit = SubmitField('Add To Order')

#     def validate_username(self, username):
#         if username.data.lower() == 'admin':
#             raise ValidationError("Can't use admin as a username! Try again.")
        
# class checkAdmin:
#     def __init__(self, message=""):
#         if not message:
#             message = 'Please choose another username.'
#         self.message = message

#     def __call__(self, form, field):
#         if field.data.lower() == 'admin':
#             raise ValidationError(self.message)
        
@app.route('/booking', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            num_of_tickets = form.num_of_tickets.data
            movie = form.movie.data


            if len(first_name) == 0 or len(last_name) == 0:
                message = "Please supply both first and last name"
            else:
                message = f'Thank you, {first_name} {last_name}. you have selected {num_of_tickets} ticket for {movie}.'

    return render_template('booking.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')