from flask import request
from .classes import Players

def doSetup(players, i):
    name = request.form["name"]
    colour = request.form["colour"]
    score = 0
    y = Players(name, colour, score, i)
    players.append(y)
    return players
