from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class TeamForm(FlaskForm):
    teamname = StringField('Teamname', validators=[DataRequired()])
    captain = StringField('Team Captain', validators=[DataRequired()])
    submit = SubmitField('Register Team')
