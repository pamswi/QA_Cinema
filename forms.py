from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateTimeLocalField, SelectField
from wtforms.validators import DataRequired

class DiscussionPost(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    movie_id = SelectField('Movie')
    topic = StringField('Topic', validators=[DataRequired()])
    comment = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')