from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateTimeLocalField, SelectField, HiddenField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    movie_id = SelectField('Movie')
    topic = StringField('Topic', validators=[DataRequired()])
    content = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    post_id = HiddenField('Post ID')
    content = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')