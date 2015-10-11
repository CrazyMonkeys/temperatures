import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class card:
    def __init__(self,iStringCard):
    if re.match("2.",iStringCard):
        pass
    elif re.match("3.",iStringCard):
        pass
    def isStrictlyGreaterThan(self, iCard):
        pass
    def isAsStrongAs(self, iCard):
        pass

class player:
    def __init__(self): 
        self.permananentCards = []
        self.currentCards = []

    def getNextCard(self): #puts 1 cards in the current, retrun value,remove from permanaent
        aPlayingCard = None
        if self.isEnoughCards(1):
            aPlayingCard = self.permananentCards.pop[0]
            self.currentCards.append(aPlayingCard)
        return aPlayingCard
            
    def doDefausse(self): #puts 3 cards in the current, do not return vlau,remove from permanaent
        if self.isEnoughCards(3):
            for i in xrange(3):
                self.currentCards.append(self.permananentCards.pop[0])

    def getCurrent(self): #returns the current cards and clean cureent
        aCardsToGive = self.currentCards
        self.currentCards = []
        return aCardsToGive
        
    def addCards(self,iStringCard):
        aCard = card(StringCard)
        self.permananentCards.append(aCard)
        
    def isEnoughCards(self, iCount): #Retruns if enough cards are left
        return len(self.permananentCards) >= iCount

class manche:
    def __init__(self,iPlayer1, iPlayer2):
        self.player1 = iPlayer1
        self.player2 = iPlayer2

    def playARound(self):

        card1 = self.player1.getNextCard()
        card2 = self.player2.getNextCard()

        if == :
            self.playBataille()
        elif 1>2: # Player 1 wins
            self.echangeCards(self.player1, self.player2)
        else: # Player 2 wins
            self.echangeCards(self.player2, self.player1)
    def playBataille(self):

    def echangeCards(self, winner, looser):
        winner.getCurrent
    def run(self): #start the game
        pass

    def run(self): #start the game



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