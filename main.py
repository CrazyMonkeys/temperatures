import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class card:
    def __init__(self,stringCard):
        pass
    def isGreaterThan(self, iCard):
        pass

class player:
    def __init__(self,iCardSring): 
        pass
    def getNextCard(self): #puts 1 cards in the current, retrun value,remove from permanaent
        pass
    def doDefausse(self): #puts 3 cards in the current, do not return vlau,remove from permanaent
        pass
    def getLostCards(self): #returns the current cards and clean cureent
        pass
    def addCards(self):
        pass
    def isEnoughCards(self, iCount): #Retruns if enough cards are left
        pass

class manche:
    def __init__(self,iPlayer1, iPlayer2):
        self.player1 = iPlayer1
        self.player2 = iPlayer2
        
    def playARound(self):
        pass
    def playBataille(self):
        pass
    def echangeCards(self):
        pass
    def run(self): #start the game
        pass
    

n = int(raw_input()) # the number of cards for player 1
aPlayer1 = player("")
for i in xrange(n):
    cardp_1 = raw_input() # the n cards of player 1
    print cardp_1
m = int(raw_input()) # the number of cards for player 2
for i in xrange(m):
    cardp_2 = raw_input() # the m cards of player 2

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."







print "PAT"