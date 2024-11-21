#from player import Player

class Card:

    def __init__(self, suit, rank, value=0):
        """
        initialzes the card object
        args: suit - the suit of the card
        rank - the rank of the card
        value - the value of the card when calculating the player's hand
        image - the image of the card
        """
        self.suit = suit
        self.rank = rank
        self.value = value
        #self.image = image

    def __repr__(self): 
        return f"{self.rank}-{self.suit} (value: {self.value})"