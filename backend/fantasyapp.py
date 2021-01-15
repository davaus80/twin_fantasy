import os

from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from application.utils.extensions import db
from application.utils.serializers import serialize_one, serialize_many
from application.models.player import Player

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "nbadatabase.db"))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/addplayer", methods=["POST"])
def add_player():
    try:
        name = request.json.get('name')
        pos = request.json.get('pos')
    except:
        return "Include name and pos", 400

    player = Player()
    registered_player = player.register_player(name, pos)
    return serialize_one(registered_player), 201

@app.route("/player/allplayers", methods=["GET"])
def get_all_players():
    player = Player()
    player_returned = player.get_all_players()
    return serialize_many(player_returned)

@app.route("/player/<int:player_id>", methods=["GET"])
def get_player(player_id):
    player = Player()
    player_returned = player.get_player_by_id(player_id)
    return serialize_one(player_returned)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Fantasy app is running"

if __name__ == "__main__":
    app.run(debug=True)