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
@app.route("/pokemon/new")
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
@app.route("/pokemon/create", methods=['POST'])
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
        return redirect('/pokemon/new')
    
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

# ==================
# EDIT POKEMON ROUTE
# ==================
# GET
@app.route("/pokemon/edit/<int:id>")
def editPokemon(id):
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

    poke_data = {
        "id" : id
    }
    poke = Pokemon.get_one_with_user(poke_data)

    return render_template("editPokemon.html", user = user, poke = poke)
# POST
@app.route("/pokemon/update/<int:id>", methods=["POST"])
def updatePokemon(id):
    # ? ==================
    # ? VALIDATE POKEMON
    # ? ==================
    if not Pokemon.validate_pokemon(request.form):
        return redirect(f"/pokemon/edit/{id}")
    
    data = {
        "id" : id,
        "name" : request.form["name"],
        "type1" : request.form["type1"],
        "type2" : request.form["type2"],
        "ability1" : request.form["ability1"],
        "ability2" : request.form["ability2"],
        "ability3" : request.form["ability3"],
        "weakness1" : request.form["weakness1"],
        "weakness2" : request.form["weakness2"],
    }

    Pokemon.update(data)
    return redirect("/dashboard")

# ==================
# DELETE POKEMON ROUTE
# ==================
@app.route("/pokemon/delete/<int:id>")
def deletePokemon(id):
    # ? ==================
    # ? VERIFY USER IS LOGGED IN
    # ? ==================
    if "user_id" not in session:
        flash("Please register/login before you proceed to the website")
        return redirect("/")
    
    data = {
        "id" : id
    }
    Pokemon.delete(data)
    return redirect("/dashboard")


# ==================
# VIEW ONE POKEMON ROUTE
# ==================
@app.route("/pokemon/view/<int:id>")
def viewPokemon(id):
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

    poke_data = {
        "id" : id
    }
    poke = Pokemon.get_one_with_user(poke_data)

    return render_template("viewOnePokemon.html", user = user, poke = poke)

# ==================
# CATCH POKEMON ROUTE
# ==================
@app.route("/pokemon/catch/<int:id>")
def catchPokemon(id):
    # ? ==================
    # ? VERIFY USER IS LOGGED IN
    # ? ==================
    if "user_id" not in session:
        flash("Please register/login before you proceed to the website")
        return redirect("/")
    
    data = {
        "user_id" : session["user_id"],
        "pokemon_id" : id
    }
    Pokemon.catchPokemon(data)
    return redirect("/dashboard")