from application import app, db
from flask import render_template, request, redirect, url_for, flash, session
from models import User, Discussion, Movie
from forms import DiscussionPost
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from datetime import datetime

'''
the following app.py file defines all known routes
'''
@app.route("/")
def home():
    return render_template ("homepage.html")

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
def view_movie():
    return render_template("movie.html")

@app.route("/listings")
def listings():
    return render_template("gallery.html")

@app.route('/newreleases', methods=['GET'])
def new_releases():
    from models import Movie  

    new_releases = Movie.query.filter_by(classic=False).all()
    
    return render_template('new_releases.html', films=new_releases)

@app.route("/classics", methods=['GET'])
def classics():
    from models import Movie  

    classics = Movie.query.filter_by(classic=True).all()

    return render_template('classics.html', films=classics)


@app.route("/serchresults")
def search_results():
    return render_template("gallery.html")

@app.route("/payment", methods=["GET", "POST"])
def payment():
    return render_template("payment.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

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


app.config['SECRET_KEY'] = 'TEMP_SECRET_KEY'    
@app.route('/discussion-board', methods=["GET","POST"])
def discussionboard():
    all_posts= Discussion.all_discussion()
    all_movies = Movie.all_movies()
    form = DiscussionPost()
    form.movie_id.choices = [(0,'Other')]
    for movie in all_movies:
        form.movie_id.choices.append(
            (movie.id, f"{movie.title}")
        )
    
    if request.method == "POST":
        if form.validate_on_submit():
            with app.app_context():
                local_datetime = datetime.now()
                post_timestamp = local_datetime.strftime("%d/%m/%Y %H:%M")
                new_comment = Discussion().new_comment(form.user_id.data, form.movie_id.data, form.topic.data, form.comment.data, post_timestamp)
                all_posts= Discussion.all_discussion()
                return render_template('discussion-board.html', all_posts=all_posts, form=form)

    return render_template('discussion-board.html', all_posts=all_posts, form=form)
