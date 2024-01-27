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
        self.user = None

        # list of users who have caught this pokemon
        self.catchers = []

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
        return is_valid

    # ==================
    # SAVE
    # ==================
    @classmethod
    def savePoke(cls, data):
        query = """
            INSERT INTO pokemons (name, type1, type2, ability1, ability2, ability3, weakness1, weakness2, user_id, created_at, updated_at) VALUES (%(name)s, %(type1)s, %(type2)s, %(ability1)s, %(ability2)s, %(ability3)s, %(weakness1)s, %(weakness2)s, %(user_id)s, NOW(), NOW());
        """
        return connectToMySQL(db).query_db(query, data)
    
    # ==================
    # GET ALL WITH USERS
    # ==================
    @classmethod
    def getAllCaught(cls, data):
        query = """
            SELECT * FROM pokemons join favorites on favorites.pokemon_id = pokemons.id join users on favorites.user_id = users.id where users.id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query, data)

        pokemons = []


        # for evey result in the dictionary of results
        for pokemon in results:
            # creating a pokemon here, at this point the user field is empty
            poke = Pokemon(pokemon)

            data ={
                "id" : pokemon['user_id']
            }
            # getting user via id from db
            creator = user.User.get_one(data)

            # adding user info from db equal to user field 
            poke.user = creator

            # add pokemon to the pokemons list with user data now populated
            pokemons.append(poke)

        return pokemons
    
    # ==================
    # GET ONE WITH USER
    # ==================
    @classmethod
    def get_one_with_user(cls, data):
        query = """
            SELECT * FROM pokemons LEFT JOIN favorites ON pokemons.id = favorites.pokemon_id LEFT JOIN users ON users.id = favorites.user_id WHERE pokemons.id = %(id)s;
        """

        results = connectToMySQL(db).query_db(query, data)

        # creating instance of pokemon object
        poke = cls(results[0])
        print(poke)

        # storing user data to pokemon
        # creator = user.User.get_one(data)
        # print(creator)
        
        # poke.user = creator

        for row in results:
            if row["users.id"] == None:
                break
            data ={
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "username" : row["username"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["created_at"],
                "updated_at" : row["updated_at"],
            }

            poke.catchers.append(user.User(data))
        
        return poke
    
    # ==================
    # UPDATE POKEMON
    # ==================
    @classmethod
    def update(cls, data):
        query = """
            UPDATE pokemons SET name = %(name)s, type1 = %(type1)s, type2 = %(type2)s, ability1 = %(ability1)s, ability2 = %(ability2)s, ability3 = %(ability3)s, weakness1 = %(weakness1)s, weakness2 = %(weakness2)s, updated_at = NOW() WHERE id = %(id)s;
        """
        return connectToMySQL(db).query_db(query, data)
    
    # ==================
    # DELETE POKEMON
    # ==================
    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM pokemons where id = %(id)s;
        """
        return connectToMySQL(db).query_db(query, data)

    # ==================
    # CATCH/FAVORITE POKEMON
    # ==================
    @classmethod
    def catchPokemon(cls, data):
        query = """
            INSERT INTO favorites (user_id, pokemon_id) VALUES (%(user_id)s, %(pokemon_id)s);
        """
        return connectToMySQL(db).query_db(query, data)
    

    # ==================
    # UNCAUGHT POKEMON
    # ==================
    @classmethod
    def uncaughtPokemon(cls, data):
        query = """
            SELECT * FROM pokemons WHERE pokemons.id NOT IN (SELECT pokemon_id FROM favorites where user_id = %(id)s);
        """

        results = connectToMySQL(db).query_db(query, data)

        pokemons = []
        print(results)
        

        # for evey result in the dictionary of results
        for pokemon in results:
            # creating a pokemon here, at this point the user field is empty
            poke = Pokemon(pokemon)

            data ={
                "id" : pokemon['user_id']
            }
            # getting user via id from db
            creator = user.User.get_one(data)

            # adding user info from db equal to user field 
            poke.user = creator

            # add pokemon to the pokemons list with user data now populated
            pokemons.append(poke)

        return pokemons

    # ==================
    # RELEASE POKEMON
    # ==================
    @classmethod
    def releasePokemon(cls, data):
        query = """
            DELETE FROM favorites where user_id = %(user_id)s and pokemon_id = %(pokemon_id)s;
        """
        return connectToMySQL(db).query_db(query, data)

    # unfavorited => relationship does not yet exist