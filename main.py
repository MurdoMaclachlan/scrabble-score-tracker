from flask import Flask, render_template, request
import libsst

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    global i,setupDone,players
    setupDone = False
    i = 1
    players = []
    return render_template("index.html")

@app.route("/setup", methods=["POST"])
def setup():
    global i,setupDone,players
    j = int(request.form["number"])
    if setupDone == True:
        libsst.doSetup(players, i)
        i += 1
    if i > j:
        global playerIds,scoreInputs,inputTypes,colours,breaks,roundNumber
        playerIds = []
        scoreInputs = []
        inputTypes = []
        colours = []
        breaks = []
        roundNumber = 1
        for i in range(4):
            if i <= len(players)-1:
                playerIds.append(players[i].idnum)
                scoreInputs.append(players[i].name)
                inputTypes.append("number")
                colours.append(players[i].colour)
                breaks.append("</br>")
            else:
                playerIds.append("")
                scoreInputs.append("")
                inputTypes.append("hidden")
                colours.append("")
                breaks.append("")
        data = {
            'id1':playerIds[0],
            'id2':playerIds[1],
            'id3':playerIds[2],
            'id4':playerIds[3],
            'input1':scoreInputs[0],
            'input2':scoreInputs[1],
            'input3':scoreInputs[2],
            'input4':scoreInputs[3],
            'type1':inputTypes[0],
            'type2':inputTypes[1],
            'type3':inputTypes[2],
            'type4':inputTypes[3],
            'colour1':colours[0],
            'colour2':colours[1],
            'colour3':colours[2],
            'colour4':colours[3],
            'break1':breaks[0],
            'break2':breaks[1],
            'break3':breaks[2],
            'break4':breaks[3],
            'roundNumber':roundNumber
        }
        return render_template("gameRound.html", **data)
    else:
        setupDone = True
        data = {
            'i':i,
            'j':str(j)
        }
        return render_template("playerSetup.html", **data)

@app.route("/game", methods=["POST"])
def game():
    global playerIds,scoreInputs,inputTypes,colours,players,breaks,roundNumber
    roundNumber += 1
    for i in range(len(players)):
        players[i].score = players[i].score + int(request.form[str(players[i].idnum)])
    if request.form["continue"] == "True":
        data = {
            'id1':playerIds[0],
            'id2':playerIds[1],
            'id3':playerIds[2],
            'id4':playerIds[3],
            'input1':scoreInputs[0],
            'input2':scoreInputs[1],
            'input3':scoreInputs[2],
            'input4':scoreInputs[3],
            'type1':inputTypes[0],
            'type2':inputTypes[1],
            'type3':inputTypes[2],
            'type4':inputTypes[3],
            'colour1':colours[0],
            'colour2':colours[1],
            'colour3':colours[2],
            'colour4':colours[3],
            'break1':breaks[0],
            'break2':breaks[1],
            'break3':breaks[2],
            'break4':breaks[3],
            'roundNumber':roundNumber
        }
        return render_template("gameRound.html", **data)
    else:
        data = {
            'id1':playerIds[0],
            'id2':playerIds[1],
            'id3':playerIds[2],
            'id4':playerIds[3],
            'input1':scoreInputs[0],
            'input2':scoreInputs[1],
            'input3':scoreInputs[2],
            'input4':scoreInputs[3],
            'type1':inputTypes[0],
            'type2':inputTypes[1],
            'type3':inputTypes[2],
            'type4':inputTypes[3],
            'colour1':colours[0],
            'colour2':colours[1],
            'colour3':colours[2],
            'colour4':colours[3],
            'break1':breaks[0],
            'break2':breaks[1],
            'break3':breaks[2],
            'break4':breaks[3]
        }
        return render_template("negativeRound.html", **data)

@app.route("/end", methods=["POST"])
def end():
    global inputTypes,colours,players,breaks
    for i in range(len(players)):
        players[i].score = players[i].score - int(request.form[str(players[i].idnum)])
    players,winners,winscores = libsst.calculateWinner(players)
    listPlayers = []
    listScores = []
    winColours = []
    winnerScores = []
    listWinners = []
    winBreaks = []
    dashes = []
    winDashes = []
    colours.clear()
    for i in range(4):
        if i <= len(players)-1:
            listPlayers.append(players[i].name + ": ")
            listScores.append(str(players[i].score))
            colours.append(players[i].colour)
            dashes.append("-")
        else:
            listPlayers.append("")
            colours.append("")
            listScores.append("")
            dashes.append("")
        if i <= len(winners)-1:
            pos = libsst.linearSearch(players, winners[i])
            listWinners.append(players[pos].name + ": ")
            winnerScores.append(str(players[pos].score))
            winColours.append(players[pos].colour)
            winBreaks.append("</br>")
            winDashes.append("-")
        else:
            listWinners.append("")
            winnerScores.append("")
            winColours.append("")
            winBreaks.append("")
            winDashes.append("")
    data = {
        'player1':listPlayers[0],
        'player2':listPlayers[1],
        'player3':listPlayers[2],
        'player4':listPlayers[3],
        'score1':listScores[0],
        'score2':listScores[1],
        'score3':listScores[2],
        'score4':listScores[3],
        'colour1':colours[0],
        'colour2':colours[1],
        'colour3':colours[2],
        'colour4':colours[3],
        'break1':breaks[0],
        'break2':breaks[1],
        'break3':breaks[2],
        'break4':breaks[3],
        'dash1':dashes[0],
        'dash2':dashes[1],
        'dash3':dashes[2],
        'dash4':dashes[3],
        'winner1':listWinners[0],
        'winner2':listWinners[1],
        'winner3':listWinners[2],
        'winner4':listWinners[3],
        'wscore1':winnerScores[0],
        'wscore2':winnerScores[1],
        'wscore3':winnerScores[2],
        'wscore4':winnerScores[3],
        'wcolour1':winColours[0],
        'wcolour2':winColours[1],
        'wcolour3':winColours[2],
        'wcolour4':winColours[3],
        'winbr1':winBreaks[0],
        'winbr2':winBreaks[1],
        'winbr3':winBreaks[2],
        'winbr4':winBreaks[3],
        'wdash1':winDashes[0],
        'wdash2':winDashes[1],
        'wdash3':winDashes[2],
        'wdash4':winDashes[3]
    }
    return render_template("end.html", **data)

if __name__ == "__main__":
    players = []
    app.run(host = "localhost", port = 3000)
