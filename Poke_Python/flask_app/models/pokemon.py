# ==================
# STANDARD IMPORTS
# ==================
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

# ==================
# CLASS IMPORTS
# ==================
from flask_app.models import user

# ==================
# REDIRECT ATTRIBUTES FOR FLASH MESSAGES
# ==================
from flask import flash

# ==================
# TABLE NAME
# ==================
db = "pokepython" 

# ==================
# POKEMON MODEL
# ==================
class Pokemon:
    def __init__(self, data): 
        self.id = data['id']
        self.name = data['name']
        self.type1 = data['type1']
        self.type2 = data['type2']
        self.ability1 = data['ability1']
        self.ability2 = data['ability2']
        self.ability3 = data['ability3']
        self.weakness1 = data['weakness1']
        self.weakness2 = data['weakness2']
        self.user_id = data['user_id']
        self.creator = None
        self.favorited = []

    # ==================
    # VALIDATIONS
    # ==================
    @staticmethod
    def validate_pokemon(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Name must be at least 2 characters long")
            is_valid = False
        if not data['type1']:
            flash("At least 1 type but be filled")
            is_valid = False
        if not data['ability1']:
            flash("At least 1 ability but be filled")
            is_valid = False
        if not data['weakness1']:
            flash("At least 1 weakness but be filled")
            is_valid = False

    # ==================
    # SAVE
    # ==================
    @classmethod
    def savePoke(cls, data):
        query = """
            INSERT INTO pokemons (name, type1, type2, ability1, ability2, ability3, weakness1, weakness2, user_id, created_at, updated_at) VALUES (%(name)s, %(type1)s, %(type2)s, %(ability1)s, %(ability2)s, %(ability3)s, %(weakness1)s, %(weakness2)s, %(user_id)s, NOW(), NOW());
        """
        return connectToMySQL(db).query_db(query, data)