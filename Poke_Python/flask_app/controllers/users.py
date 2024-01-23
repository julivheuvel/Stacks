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

# ! =================================================
# ! =================================================

# ==================
# INDEX ROUTE
# ==================
@app.route("/")
def index():
    return render_template("logReg.html")

# ==================
# REGISTER ROUTE
# ==================
@app.route("/register", methods=['POST'])
def register():
    # ? ==================
    # ? VALIDATE INFO
    # ? ==================
    if not User.validate_user(request.form):
        return redirect("/")    
    # ? ==================
    # ? VERIFY AVAILABLE EMAIL
    # ? ==================
    verify_email = {
        "email" : request.form["email"]
    }
    if User.get_by_email(verify_email):
        flash("Email already exists. Please use different email to complete registration")
        return redirect('/')    
    # ? ==================
    # ? HASH PASSWORD
    # ? ==================
    hashbrowns = bcrypt.generate_password_hash(request.form["password"])
    # ? ==================
    # ? CREATE DICTIONARY TO PASS TO SAVE CLASSMETHOD
    # ? ==================
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "username" : request.form["username"],
        "email" : request.form["email"],
        "password" : hashbrowns,
    }
    new_user = User.save(data)
    # ? ==================
    # ? SAVE USER_ID TO SESSION
    # ? ==================
    session["user_id"] = new_user
    return redirect("/dashboard")


# ==================
# LOGIN ROUTE
# ==================
@app.route("/login", methods=['POST'])
def login():
    # ? ==================
    # ? EDGE CASE FOR EMPTY FIELDS
    # ? ==================
    if not User.validate_login(request.form):
        return redirect("/")    
    

    # ? ==================
    # ? VERIFY EXISTING USERNAME
    # ? ==================
    data = {
        "username" : request.form["username"]
    }
    user_in_db = User.get_by_username(data)
    if not user_in_db:
        flash("Invalid Credentials")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Credentials")
        return redirect("/")
    # ? ==================
    # ? SAVE USER_ID TO SESSION
    # ? ==================
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

# ==================
# DASHBOARD ROUTE
# ==================
@app.route("/dashboard")
def dashboard():
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
    return render_template("dashboard.html", user = user)

# ==================
# LOGOUT ROUTE
# ==================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")