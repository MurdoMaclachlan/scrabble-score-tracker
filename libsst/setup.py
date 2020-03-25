from flask import request
from .classes import Players

def doSetup(players, i):

    #gets player data
    name = request.form["name"]
    colour = request.form["colour"]
    score = 0

    #declares instance of the "Players" class and adds it to array of records
    y = Players(name, colour, score, i)
    players.append(y)

    return players
