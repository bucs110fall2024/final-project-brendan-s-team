#from player import Player
import pygame

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
        self.image = (f'assets/{self.rank}-{self.suit}.png')
        self.CARD_SIZE = (125, 181.5)

    def value(self):
        return self.value

    def __repr__(self): 
        """
        returns the card as a readable string
        """
        return f"{self.rank}-{self.suit} (value: {self.value}) (image: {self.image})"

    def load_image(self): 
        """
        loads the image onto the screen, and scales it down to size on the screen
        """
        return pygame.transform.scale(pygame.image.load(self.image), self.CARD_SIZE)
