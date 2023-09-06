
from application import app, db
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from models import User
from werkzeug.security import check_password_hash, generate_password_hash
from models import Movie, Screening, Discussion
from forms import DiscussionPost, PayForm, BasicForm
from datetime import date, timedelta

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'    

'''
the following app.py file defines all known routes
'''
@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/openingtimes")
def opening_times():
    return render_template("opening.html")

@app.route("/classifications")
def classifications():
    return render_template("classification.html")

@app.route("/screens")
def screens():
    return render_template("screens.html")

@app.route("/services")
def cinema_services():
    return render_template("services.html")

@app.route("/movies/<int:movie_id>")
def view_movie(movie_id):
    current_date =date.today()
    seven_days_from_now = current_date + timedelta(days=7)
    movie = Movie.query.get(movie_id)
    return render_template("movie.html", movie=movie)

@app.route("/api/movies/<int:movie_id>")
def api_view_screenings(movie_id):
    selected_day = request.args.get('day')
    screenings = Screening.query.filter_by(movie_id=movie_id, day=selected_day).all()
    screening_data = []
    
    for screening in screenings:
        screening_data.append({
            'id': screening.id,
            'title': screening.movie_id,
            'screen_number': screening.screen_id,
            'time': screening.time,
            'current_capacity': screening.current_capacity

        })
    
    if not screenings:
        return 'There are currently no showings of this film'
    
    return jsonify(screening_data)


@app.route("/listings")
def listings():
    return render_template("gallery.html")

@app.route('/newreleases', methods=['GET'])
def new_releases(): 

    new_releases = Movie.get_current_movies()
    return render_template('new_releases.html', films=new_releases)

@app.route("/classics", methods=['GET'])
def classics():

    classics = Movie.get_classic_movies()
    
    return render_template('classics.html', films=classics)


@app.route("/serchresults")
def search_results():
    # currently hardcoded, however once search bar is designed it will accept dynamic input
    user_input="the"
    results = Movie.search(user_input)
    for result in results:
        print(result.title)

    return render_template("classics.html", films=results)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    message = ""
    form = PayForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        card_number = form.card_number.data
        expiry_date = form.expiry_date.data
        card_cvc = form.cvc_number.data
        update_user = User.add_payment(session["username"], first_name, last_name, address, card_number, expiry_date, card_cvc)

        message= "payment received"

    return render_template('payment.html', form=form, message=message)


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

        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # below we retrieve user by username and check if the password is correct
        user = User.retrieve_user(username)
        if user is not None:
            if check_password_hash(user.password, password) == True:
                session["username"] = user.username
            else:
                flash("incorrect username and/or password")
                return redirect ("/login")
        return redirect ("/")
    
    return render_template ("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        # Clear the user's session
        session.clear()
        return redirect("/")
    return render_template("logout.html")

        
@app.route('/booking', methods=['GET', 'POST']) # AKBER
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