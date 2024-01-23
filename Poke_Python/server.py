from flask_app import app
# importing controllers

from flask_app.controllers import pokemons, users


if __name__ == "__main__":
    app.run(debug=True)