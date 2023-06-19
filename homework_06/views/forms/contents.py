from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ContentForm(FlaskForm):
    name = StringField(
        label="Content name:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
