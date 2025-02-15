from random import shuffle 
#to do:
'''
    handle ties (war)
        handle tieBreaker recursion
    make variable to store round winner?
    make variable to store round winnings?
    refactor toWinPiles to use roundChecker

'''
    

#functions
def start():

    #deck
    def buildDeck(): #works #builds deck and shuffles it for first use
        suits = ["hearts", "diamonds", "spades", "clubs"]
        ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
        
        deck  = [(suit, rank) for suit in suits for rank in ranks] #builds the deck
        shuffle(deck) #shuffles the new deck...in case you couldn't tell
        return deck
        
    def deal(): #works deals deck into 2 decks while alternating between players. dels original deck per index.
        switch = True
        while len(wholeDeck) > 0:
            if switch == True:
                cpuDeck.append(wholeDeck[0])
                del wholeDeck[0]
            else:
                playerDeck.append(wholeDeck[0])
                del wholeDeck[0]
            switch = not switch
    wholeDeck = buildDeck()
    deal()


def roundChecker():# check round winner
    tieCount = 0
    def tieBreaker():
       
        player = max(playerDeck[1:4])
        cpu = max(cpuDeck[1:4])
        if cpu > player:
           return 'cpu'
        elif player > cpu:
           return 'player'
        else:
            return tieBreaker(tieCount)



    if playerDeck[0] > cpuDeck[0]:
        return 'player'
    elif cpuDeck[0] > playerDeck[0]:
        return 'cpu'
    else:
        return tieBreaker(tieCount)


def deckToPile(): # doesn't handle ties. Win handling needs to be offloaded
    if playerDeck[0] > cpuDeck[0]:
        playerWinPile.append(playerDeck[0])
        del playerDeck[0]
        playerWinPile.append(cpuDeck[0])
        del cpuDeck[0]

    elif cpuDeck[0] > playerDeck[0]:
        cpuWinPile.append(playerDeck[0])
        del playerDeck[0]
        cpuWinPile.append(cpuDeck[0])
        del cpuDeck[0]

def shuffler(): #shuffles current deck in place
    shuffle(cpuDeck)
    shuffle(playerDeck)

#card

playerDeck = []
playerWinPile = []
cpuDeck = []
cpuWinPile = []
#deck = buildDeck()

start()
print (cpuDeck)
print("\n")
print (playerDeck)

