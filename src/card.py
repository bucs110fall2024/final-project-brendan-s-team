import pygame

class Card:

    def __init__(self, suit, rank, value):
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
        self.CARDSIZE = (125, 181.5)
        self.back = 'assets/BACK.png'

    def __repr__(self): 
        """
        prints the card as a string readable in the console
        args: self
        return: the card as a readable string
        """
        return f"{self.rank}-{self.suit} (value: {self.value}) (image: {self.image})"

    def load_image(self): 
        """
        loads the image onto the screen, and scales it down to size on the screen
        args: self
        return: returns the transformed scale and loaded image
        """
        return pygame.transform.scale(pygame.image.load(self.image), self.CARDSIZE)
