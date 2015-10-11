import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

global LOGGING
LOGGING = False

def cprint(iString):
    if LOGGING:
        print iString

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
    def __repr__(self):
        return str(self.internal)
    def __str__(self):
        return self.__repr__()

class player:
    def __init__(self): 
        self.permananentCards = []
        self.currentCards = []

    def getNextCard(self): #puts 1 cards in the current, retrun value,remove from permanaent
        aPlayingCard = None
        if self.isEnoughCards(1):
            aPlayingCard = self.permananentCards.pop(0)
            self.currentCards.append(aPlayingCard)
        return aPlayingCard
            
    def doDefausse(self): #puts 3 cards in the current, do not return vlau,remove from permanaent
        if self.isEnoughCards(3):
            for i in xrange(3):
                self.currentCards.append(self.permananentCards.pop(0))

    def getCurrent(self): #returns the current cards and clean cureent
        aCardsToGive = self.currentCards
        self.currentCards = []
        return aCardsToGive
        
    def addCard(self,iCard):
        self.permananentCards.append(iCard)
        
    def addCards(self,iCardList):
        self.permananentCards.extend(iCardList)


        
    def isEnoughCards(self, iCount): #Retruns if enough cards are left 
        return len(self.permananentCards) >= iCount
        
    def __repr__(self):
        aPermanent = ','.join([ i.__repr__() for i in self.permananentCards])
        aCurrent = ','.join([ i.__repr__() for i in self.currentCards])
        return 'Perm: '+aPermanent
    def __str__(self):
        return self.__repr__()

class manche:
    def __init__(self,iPlayer1, iPlayer2):
        self.player1 = iPlayer1
        self.player2 = iPlayer2
        self.count = 0

    def playARound(self):
        cprint("=======================")
        cprint(self.player1)
        cprint(self.player2)


        if self.player1.isEnoughCards(1) and self.player2.isEnoughCards(1):
            card1 = self.player1.getNextCard()
            card2 = self.player2.getNextCard()
            # enough card to continue
            if card1.isAsStrongAs(card2):
                cprint("Bataille")
                # egality
                is_bataille_Possible = self.playBataille()
                if not is_bataille_Possible:
                    cprint ("Bataille pas possibvle")
                    return "PAT"

            elif card1.isStrictlyGreaterThan(card2):
                cprint("Player 1 wins")
                # Player 1 wins
                self.echangeCards(self.player1, self.player2)

            else:
                cprint("Player 2 wins")
                # Player 2 wins
                self.echangeCards(self.player2, self.player1)
                
            
                
        if not self.player1.isEnoughCards(1):
            cprint("Not enough cards 2 wins")
            return "2"
        elif not self.player2.isEnoughCards(1):
            cprint("Not enough cards 1 wins")
            return "1"

    def playBataille(self):
        if self.player1.isEnoughCards(4) and self.player2.isEnoughCards(4):
            self.player1.doDefausse()
            self.player2.doDefausse()
            self.playARound()
            return True
        else:
            return False

    def echangeCards(self, winner, looser):
        winner.addCards(winner.getCurrent())
        winner.addCards(looser.getCurrent())



    def run(self): #start the game
        LOGGING = True
        cprint( "runsStart")
        winner = None
        aCounter = 0
        if aCounter > 10:
            LOGGING = False
        while not winner and aCounter<1000:
            cprint("Round: "+str(self.count))
            self.count += 1
            winner = self.playARound()
            aCounter +=1 

        if winner == "PAT":
            print "PAT"
        else:
            print winner +' ' +str(self.count)


n = int(raw_input()) # the number of cards for player 1
aPlayer1 = player()
aPlayer2 = player()
for i in xrange(n):
    cardp_1 = raw_input() # the n cards of player 1
    aPlayer1.addCard(card(cardp_1))
m = int(raw_input()) # the number of cards for player 2
for i in xrange(m):
    cardp_2 = raw_input() # the m cards of player 2
    aPlayer2.addCard(card(cardp_2))

aManche = manche (aPlayer1, aPlayer2)
aManche.run()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."