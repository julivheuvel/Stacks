# ==================
# STANDARD IMPORTS
# ==================
from flask_app import app
from flask import render_template, request, redirect, session

# ==================
# MODEL IMPORTS
# ==================
from flask_app.models.user import User
from flask_app.models.pokemon import Pokemon

# ==================
# BCRYPT IMPORTS
# ==================
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ==================
# REDIRECT ATTRIBUTES FOR FLASH MESSAGES
# ==================
from flask import flash


# ==================
# NEW POKEMON ROUTE
# ==================
# GET
@app.route("/new/pokemon")
def newPokemon():
    # ? ==================
    # ? VERIFY USER IS LOGGED IN
    # ? ==================
    if "user_id" not in session:
        flash("Please register/login before you proceed to the website")
        return redirect("/")    
    data = {
        "id" : session["user_id"]
    }
    user = User.get_one(data)
    # 
    return render_template("new_pokemon.html", user = user)

# POST
@app.route("/create/pokemon", methods=['POST'])
def createPokemon():
    # ? ==================
    # ? VERIFY USER IS LOGGED IN
    # ? ==================
    if "user_id" not in session:
        flash("Please register/login before you proceed to the website")
        return redirect("/")    

    # ? ==================
    # ? VALIDATE TREE INFO
    # ? ==================
    if not Pokemon.validate_pokemon(request.form):
        print("Invalid!!")
        return redirect('/new/pokemon')
    
    data = {
        "name" : request.form["name"],
        "type1" : request.form["type1"],
        "type2" : request.form["type2"],
        "ability1" : request.form["ability1"],
        "ability2" : request.form["ability2"],
        "ability3" : request.form["ability3"],
        "weakness1" : request.form["weakness1"],
        "weakness2" : request.form["weakness2"],
        "user_id" : session["user_id"]
    }
    Pokemon.savePoke(data)
    return redirect("/dashboard")