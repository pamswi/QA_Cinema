from application import app, db
from flask import render_template, request, redirect, url_for, flash, session
from models import User
from werkzeug.security import check_password_hash, generate_password_hash


'''
the following app.py file defines all known routes
'''

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
        return redirect ("/")
    
    return render_template ("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect ("/")

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'    
@app.route('/discussion-board', methods=["GET","POST"])
def discussionboard():
    from forms import DiscussionPost
    from models import Discussion
    all_posts= Discussion.all_discussion()
    form = DiscussionPost()

    if request.method == "POST":
        if form.validate_on_submit():
            with app.app_context():
                new_post = Discussion(
                    user_id = form.user_id.data,
                    movie_id = form.user_id.data,
                    topic = form.topic.data,
                    comment = form.comment.data,
                    timestamp = form.timestamp.data
                )
                db.session.add(new_post)
                db.session.commit()
                all_posts= Discussion.all_discussion()

    return render_template('discussion-board.html', all_posts=all_posts, form=form)
