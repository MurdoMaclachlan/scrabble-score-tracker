from .searches import binarySearch
from .sorts import bubbleSort

def calculateWinner(players):
  maxScore = players[0].score
  winners = []
  winids = []
  winscores = []

  #searches list for the player with the highest score

  players = bubbleSort(players)

  for i in range(len(players)):

    #if multiple players have the highest score, all are added as winners
    if players[i].score == maxScore:
      winners.append(players[i].name)
      winids.append(players[i].idnum)

    #if a new highest score is found, the old one is overwritten and all winners are removed from the win list
    elif players[i].score > maxScore:
      maxScore = players[i].score
      winners.clear()
      winids.clear()
      winners.append(players[i].name)
      winids.append(players[i].idnum)

  for i in range(len(winids)):

      #binary search method works because winid list is by its nature sorted
      pos = binarySearch(players, winids[i])
      winscores.append(players[pos].score)

  return players, winners, winscores
