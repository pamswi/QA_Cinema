from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired

class DiscussionPost(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    movie_id = IntegerField('Movie ID')
    topic = StringField('Topic', validators=[DataRequired()])
    comment = StringField('Message', validators=[DataRequired()])
    timestamp = DateTimeLocalField('Timestamp', format='%Y-%m-%d %H:%M:%S')
    send = SubmitField('Send')