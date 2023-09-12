
from application import app, db
from flask import render_template, request, redirect, url_for, flash, session, jsonify
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
# from wtforms.validators import ValidationError, DataRequired, Length
from models import User, Discussion, Movie, Screening, Booking, BookingDetail
from forms import PostForm
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from datetime import datetime
from forms import PostForm, PayForm, BookingForm
from datetime import date, timedelta
from filter.swearwords import swearwords
import re

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'    

'''
the following app.py file defines all known routes
'''
@app.route("/")
def home():
    all_films = Movie.query.all()
    username = session["username"]
    print(username)
    return render_template ("homepage.html", films=all_films)

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
    print(session)
    message = ""
    form = PayForm()

    tickets = session.get('tickets', [])
    total_price = session.get('total_price', 0)
    print(tickets, total_price)
     #<ALEX
    screening_id = request.args.get('screening_id')
    screening = Screening.query.get(screening_id)  
    movie_id = screening.movie_id
    selected_date = screening.day
    time = screening.time
    current_capacity = screening.current_capacity
    movie = Movie.query.get(movie_id)
    movie_title = movie.title
    movie_poster = movie.poster 
    #/ALEX>

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        card_number = form.card_number.data
        expiry_date = form.expiry_date.data
        card_cvc = form.cvc_number.data
        update_user = User.add_payment(session["username"], first_name, last_name, address, card_number, expiry_date, card_cvc)

        total_tickets_booked = sum(quantity for _, quantity in tickets)
        screening.current_capacity -= total_tickets_booked
        db.session.commit()
    

    


    return render_template(
            'payment.html', 
            form=form, 
            message=message, 
            movie_title=movie_title, 
            movie_poster=movie_poster, 
            selected_date=selected_date,
            time=time, 
            current_capacity=current_capacity,
            tickets=tickets,              
            total_price=total_price      
            )


@app.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # password validation: https://www.geeksforgeeks.org/python-program-check-validity-password/
        if User.check_unique_username(username) != True:
            print("username already exists")
        elif password != confirmation:
            print("password & confirm password do not match")
        else:
            if (
                len(password) >= 8 and               
                re.search(r'[a-z]', password) and   
                re.search(r'[A-Z]', password) and   
                re.search(r'[0-9]', password) and  
                re.search(r'[_@$]', password)      
            ):
                password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                new_user = User.add_user(username, email, password_hash)
                print("sign up successful")

                return redirect("/login")
            else:
                print("password does not meet security requirements")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # below we retrieve user by username and check if the password is correct
        user = User.retrieve_user(username)

        if user is None:
            print("no account associated with this username - please sign up")
            return render_template ("signup.html")
        elif user is not None:
            if check_password_hash(user.password, password) == True:
                session["username"] = user.username
                session["user_id"] = user.id
                print("successfully logged in")
            else:
                print("incorrect username and/or password")
                return redirect ("/login")
        return redirect ("/")
    
    return render_template ("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        # Clear the user's session
        session.clear()
        print("successfully logged out")
        return redirect("/")
    return render_template("logout.html")

@app.route('/forum', methods=["GET", "POST"])
def forum():
    # print(session["username"])
    all_posts= Discussion.all_posts()
    postform = PostForm()
    all_comments=Discussion.all_comments()
    all_movies = Movie.all_movies()

    # creating choices for movie dropdown
    postform.movie_id.choices = [(0,'Other')]
    for movie in all_movies:
        postform.movie_id.choices.append(
            (movie.id, f"{movie.title}")
        )
    
    def contains_swearword(text):
        text = text.lower()  #converts all text to lower e.g. SwEaRwOrd = swearword can be caught.
        return any(word in text.split() for word in swearwords)

    if request.method == "POST":
        if postform.validate_on_submit():
            username = session["username"]
            responding_to = request.form.get("responding_to")
            movie_id = postform.movie_id.data
            topic = postform.topic.data
            content = postform.content.data
            local_datetime = datetime.now()
            timestamp = local_datetime.strftime("%d/%m/%Y %H:%M")
            
            found_inappropriate_language = False 

            if contains_swearword(topic):
                flash("Your topic contains inappropriate language!", "error")
                found_inappropriate_language = True

            if contains_swearword(content):
                flash("Your comment contains inappropriate language!", "error")
                found_inappropriate_language = True 

            if not found_inappropriate_language:
                flash("Comment posted successfully!", "success")
                add_post= Discussion.new_post(username, movie_id, topic, responding_to, content, timestamp)
            
            return redirect(url_for('forum'))

    return render_template("forum.html", all_posts=all_posts, postform=postform, all_comments=all_comments)






@app.route('/booking', methods=['GET', 'POST'])
def book_movie():
    form = BookingForm()  
     #<ALEX
    screening_id = request.args.get('screening_id')
    screening = Screening.query.get(screening_id)  
    movie_id = screening.movie_id
    selected_date = screening.day
    time = screening.time
    current_capacity = screening.current_capacity

    movie = Movie.query.get(movie_id)
    movie_title = movie.title
    movie_poster = movie.poster 
    #/ALEX>

    if form.validate_on_submit():
        ticket_prices = {'Adult': 10.0,'Kids': 7.5,'Concession': 15.0}        
        total_price = 0
        tickets = [
            ("Adult", form.Adult.data),
            ("Kids", form.Child.data),
            ("Concession", form.Concession.data)
        ]
        for ticket_type, quantity in tickets:
            total_price += ticket_prices[ticket_type] * quantity

        booking = Booking.book_movie(
            user_id=session["user_id"],
            screening_id=request.args.get('screening_id'),
            total_price=total_price
        ) 
        
        for ticket_type, quantity in tickets:

            BookingDetail.add_booking_detail(
                booking_id=booking.id,
                ticket_type=ticket_type,
                quantity=quantity,
                price=ticket_prices[ticket_type]
            )
        session['tickets'] = tickets
        session['total_price'] = total_price
        return redirect(url_for('payment', screening_id=screening_id))
   
    return render_template(
        'booking.html', 
        movie_title=movie_title, 
        movie_poster=movie_poster, 
        screening_id=screening_id, 
        selected_date=selected_date,
        movie_id=movie_id, 
        time=time, 
        current_capacity=current_capacity, 
        form=form
    )
     
