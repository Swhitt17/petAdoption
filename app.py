from flask import Flask, request,render_template,redirect,flash,session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db, Pet
from forms import PetForm, EditForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "eatmorchikin123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



context = app.app_context()
context.push()
connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    """Shows list of pets"""
    pets = Pet.query.all()
    return render_template("list.html", pets=pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():
   """Shows and Handles form for new pet"""
   form = PetForm()
   if form.validate_on_submit():
       new_pet = Pet(
       name = form.name.data,
       species = form.species.data,
       photo_url = form.photo_url.data,
       age = form.age.data,
       notes = form.notes.data)
      
       db.session.add(new_pet)
       db.session.commit()
       flash(f"{new_pet.name} added")
       return redirect('/')
   else:
       return render_template("add_form.html", form=form)
   
   
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Shows info about pet and edit form"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} changed")
        return redirect('/')

    else:
        return render_template("edit_form.html", form=form, pet=pet)


   

