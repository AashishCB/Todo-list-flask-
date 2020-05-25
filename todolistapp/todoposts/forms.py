from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddJob(FlaskForm):

    text = StringField('Add work', validators=[DataRequired()])
    submit = SubmitField('Add')
