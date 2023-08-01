import random
from Card import Card

class Deck:

    def __init__(self):
        self.generateDeck()
        self.shuffle()


    
    #shuffles the deck of cards by making 150 random swaps
    def shuffle(self):
        for i in range(1,151):

            # declare a variable called index1 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            index1=random.randint(0,len(self.deck) -1 )

            # declare a variable called index2 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            index2=random.randint(0,len(self.deck) -1)

            # declare a variable called temp and assign it to the element of the deck of Cards located at index1
            temp=self.deck[index1]

            # set the element of the deck of Cards located at index1 to the element of the deck located at index2
            self.deck[index1]=self.deck[index2]

            # set the element of the deck of Cards located at index2 to temp
            self.deck[index2]=temp

        
   #generates a deck of un-shuffled cards

    def generateDeck(self):
        self.deck=[]
        suits=['♥', '♦', '♣', '♠']
        
        #returns a set of 52 unique cards to self.deck list
        
        for suit in suits:
            for num in range(1,14):
                self.deck.append(Card(suit,num))
        return self.deck

    
    #draws a card from the deck and return a card object
    
    def drawCard(self):

        #pops a card only if there are cards remaining in the deck
        if len(self.deck)>0:
            return self.deck.pop(0)
        else:
            return None
        
    
    
    #returns the number of cards left in the deck as an int
    def cardsLeft(self):
        return (len(self.deck))

    
        