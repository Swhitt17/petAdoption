from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField,BooleanField
from wtforms.validators import InputRequired, Optional,NumberRange,URL


class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name cannot be blank")])
    species = SelectField("Species", choices=[("cat","Cat"), ("dog","Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Link to pet photo", validators= [Optional(),URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0,max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditForm(FlaskForm):
    photo_url = StringField("Link to pet photo", validators= [Optional(),URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Avaliable?", validators=[ Optional()])
    