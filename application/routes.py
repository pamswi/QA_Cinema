from application import app
from flask import render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from models import User
from werkzeug.security import check_password_hash, generate_password_hash


'''
the following app.py file defines all known routes
'''
# @app.route("/")
# def home():
#     return render_template ("homepage.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        if User.check_unique_username != True:
            flash("user already exists")
        
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        new_user = User.add_user(username, email, password_hash)

        return render_template("login.html")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        session["username"] = request.form["username"]
        username = request.form.get("username")
        password = request.form.get("password")

        # below we retrieve user by username and check if the password is correct
        user = User.retrieve_user(username)
        if user is not None:
            if check_password_hash(user.password, password):
                session["username"] = user.username

            print(session["username"])
        return redirect ("/")
    
    return render_template ("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        # Clear the user's session
        session.clear()
        return redirect("/")
    return render_template("logout.html")

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