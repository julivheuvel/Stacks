# ==================
# STANDARD IMPORTS
# ==================
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

# ==================
# CLASS IMPORTS
# ==================
from flask_app.models import pokemon

# ==================
# REDIRECT ATTRIBUTES FOR FLASH MESSAGES
# ==================
from flask import flash

# ==================
# REGEX IMPORTS
# ==================
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# ==================
# BCRYPT IMPORTS
# ==================
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ==================
# TABLE NAME
# ==================
db = "pokepython" 

# ==================
# USER MODEL
# ==================
class User:
    def __init__(self, data): 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ==================
    # VALIDATIONS
    # ==================
    @staticmethod
    def validate_user(data):
        is_valid = True
        if not data["first_name"]:
            flash("First Name must be filled in!")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters long!")
            is_valid = False
        if not data["last_name"]:
            flash("Last Name must be filled in!")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 2 characters long!")
            is_valid = False
        if not data["username"]:
            flash("Userame must be filled in!")
            is_valid = False
        if len(data['username']) < 2:
            flash("Last Name must be at least 2 characters long!")
            is_valid = False
        if not data["password"]:
            flash("Password must be filled in!")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters long!")
            is_valid = False
        if not data["email"]:
            flash("Email must be filled in!")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Email is not valid!")
            is_valid = False
        if not data["confirm_password"]:
            flash("Confirm Password must be filled in!")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords must match!")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        if not data["username"]:
            flash("Username must be filled in!")
            is_valid = False
        if not data["password"]:
            flash("Password must be filled in!")
            is_valid = False
        return is_valid
    
    # ==================
    # CREATE USER
    # ==================
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, username, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(db).query_db(query, data)
    
    # ==================
    # GET ONE BY EMAIL 
    # ==================
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False    
        return cls(results[0])    
    
    # ==================
    # GET ONE BY USERNAME 
    # ==================
    @classmethod
    def get_by_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False    
        return cls(results[0])    
    
    # ==================
    # GET ONE USER 
    # ==================
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return None
        else:
            return User(results[0])

