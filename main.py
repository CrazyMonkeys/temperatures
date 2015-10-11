import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of cards for player 1
for i in xrange(n):
    cardp_1 = raw_input() # the n cards of player 1
m = int(raw_input()) # the number of cards for player 2
for i in xrange(m):
    cardp_2 = raw_input() # the m cards of player 2

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

class card:
    def __init__(self,stringCard):
    def isGreaterThan(self, iCard):

class player:
    def __init__(self,iCardSring): 
    def getNextCard(self): #puts 1 cards in the current, retrun value,remove from permanaent
    def doDefausse(self): #puts 3 cards in the current, do not return vlau,remove from permanaent
    def getLostCards(self): #returns the current cards and clean cureent
    def addCards(self):
    def isEnoughCards(self, iCount): #Retruns if enough cards are left

class manche:
    def __init__(self,iPlayer1, iPlayer2):
        self.player1 = iPlayer1
        self.player2 = iPlayer2
        
    def playARound(self): 
    def playBataille(self):
    def echangeCards(self):
    def run(self): #start the game
    




print "PAT"
