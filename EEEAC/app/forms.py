from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])

class AddForm(FlaskForm):
    add = StringField('Add', validators=[DataRequired()])
