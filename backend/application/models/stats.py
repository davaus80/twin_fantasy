from application.utils.extensions import db
from application.models import Player

class Stat(db.Model):
    stat_id = db.column(db.Integer(), unique=True, nullable=False, primary_key=True)
    player_id = db.column(db.Integer(), nullable=False, foreign_key=True)
    date = db.column(db.Date(), nullable=False)
    pts = db.column(db.Integer(), nullable=False)
    rebs = db.column(db.Integer(), nullable=False)
    asts = db.column(db.Integer(), nullable=False)

    def __repr__(self):
        return "<{0}: {1} ({2})>".format(self.player_id, self.name, self.position)