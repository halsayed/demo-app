from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskCreate(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(100)])
    description = StringField('Description', validators=[Length(200)])
    submit = SubmitField('Add')
