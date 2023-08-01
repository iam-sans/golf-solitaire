class Card:
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
        
    #using getters to get the value and suit from the card
     
    def getSuit(self):
        return self.suit
    
    def getValue(self):
        return self.value

    #returning a concatenation of value and suit
    
    def __str__(self):
        return str(self.value) +str(self.suit)

