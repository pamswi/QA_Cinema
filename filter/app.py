from flask import Flask, render_template
from swearwords import swearwords
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'akber'  # NEED TO IMPLMENT OS SECRET FUNCTION LATER!!!!!


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')

def contains_swearword(text):
    text = text.lower()  #converts all text to lower e.g. SwEaRwOrd = swearword can be caught.
    return any(word in text.split() for word in swearwords)

@app.route('/forum', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    message = None
    if form.validate_on_submit():
        comment = form.comment.data
        if contains_swearword(comment):
            message = 'Your comment contains inappropriate language!'
        else:
            message = 'Comment posted successfully!'
    return render_template('forum.html', form=form, message=message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)