from application.utils.extensions import db
from sqlalchemy_serializer import SerializerMixin

class Player(db.Model, SerializerMixin):
    __tablename__ = 'Player'
    player_id = db.Column('player_id',db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column('name', db.String(30), unique=True, nullable=False)
    position = db.Column('position', db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return "<{0}: {1} ({2})>".format(self.player_id, self.name, self.position)

    def get_player_by_name(self, name):
        existing_player = Player.query.filter(Player.name==name).first()
        return existing_player

    def get_player_by_id(self, id):
        existing_player = Player.query.filter(Player.player_id==id).first()
        return existing_player

    def get_all_players(self):
        all_players = Player.query.filter().all()
        return all_players

    def register_player(self, name, pos):
        if (self.get_player_by_name(name) != None):
            return Player.query.filter(Player.name==name).first()

        newplayer = Player(name=name, position=pos)
        db.session.add(newplayer)
        db.session.commit()
        return newplayer
