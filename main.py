import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class card:
    def __init__(self,iStringCard):
        if re.match("2.",iStringCard):
            self.internal = 2
        elif re.match("3.",iStringCard):
            self.internal = 3
        elif re.match("4.",iStringCard):
            self.internal = 4
        elif re.match("5.",iStringCard):
            self.internal = 5
        elif re.match("6.",iStringCard):
            self.internal = 6
        elif re.match("7.",iStringCard):
            self.internal = 7
        elif re.match("8.",iStringCard):
            self.internal = 8
        elif re.match("9.",iStringCard):
            self.internal = 9
        elif re.match("10.",iStringCard):
            self.internal = 10
        elif re.match("J.",iStringCard):
            self.internal = 11
        elif re.match("Q.",iStringCard):
            self.internal = 12
        elif re.match("K.",iStringCard):
            self.internal = 13
        elif re.match("A.",iStringCard):
            self.internal = 14
        else:
            raise Exception("Wrong stringCard in card constructor")

    def isStrictlyGreaterThan(self, iCard):
        return self.internal > iCard.internal
    def isAsStrongAs(self, iCard):
        return self.internal == iCard.internal

class player:
    def __init__(self,iCardSring): 
        pass
    def getNextCard(self): #puts 1 cards in the current, retrun value,remove from permanaent
        pass
    def doDefausse(self): #puts 3 cards in the current, do not return vlau,remove from permanaent
        pass
    def getCurrent(self): #returns the current cards and clean cureent
        pass
    def addCards(self):
        pass
    def isEnoughCards(self, iCount): #Retruns if enough cards are left
        pass

class manche:
    def __init__(self,iPlayer1, iPlayer2):
        self.player1 = iPlayer1
        self.player2 = iPlayer2
        self.count = 0

    def playARound(self):
        card1 = self.player1.getNextCard()
        card2 = self.player2.getNextCard()

        if self.player1.isEnoughCards(1) and self.player2.isEnoughCards(1):
            # enough card to continue
            if card1.isAsStrongAs(card2):
                # egality
                is_bataille_Possible = self.playBataille()
                if not is_bataille_Possible:
                    return "PAT"

            elif card1.isStrictlyGreaterThan(card2):
                # Player 1 wins
                self.echangeCards(self.player1, self.player2)

            else:
                # Player 2 wins
                self.echangeCards(self.player2, self.player1)
                
        elif not self.player1.isEnoughCards(1):
            return "1"
        elif not self.player2.isEnoughCards(1):
            return "2"

    def playBataille(self):
        if self.player1.isEnoughCards(4) and self.player2.isEnoughCards(4):
            self.player1.doDefausse()
            self.player2.doDefausse()
            self.playARound()
        else:
            return False

    def echangeCards(self, winner, looser):
        winner.addCards(winner.getCurrent())
        winner.addCards(looser.getCurrent())

    def run(self): #start the game
        while not winner:
            self.count += 1
            winner = self.playARound()

        if winner == "PAT":
            print "PAT"
        else:
            print winner + self.count



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