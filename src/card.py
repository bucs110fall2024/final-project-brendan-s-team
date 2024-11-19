from player import Player
import random

class Card:

    def __init__(self, suit, rank, value=0):
        """
        initialzes the card object
        args: suit - the suit of the card
        rank - the rank of the card
        value - the value of the card when calculating the player's hand
        """
        self.suit = suit
        self.rank = rank
        self.value = value

    def make_deck():
        """
        makes a list representing a deck of cards
        args: none
        returns: deck - a list representing a deck of cards
        """
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["H", "D", "C", "S"]
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(rank + "-" + suit)
        random.shuffle(deck)
        return deck
