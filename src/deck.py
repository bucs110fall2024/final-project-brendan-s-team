from src.card import Card
import random

class Deck:
    def __init__(self):
        """
        inits the deck object
        """
        self.deck = []
    
    def make_deck(self):
        """
        uses nested for loops and lists to create a full 52 card deck out of card objects and shuffles it
        """
        suits = ['H', 'D', 'C', 'S']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        deck = []
        for suit in suits:
            for rank, value in zip(ranks, values):
                card = Card(suit, rank, value) 
                self.deck.append(card) 
        random.shuffle(self.deck)
    
    def deal_card(self):
        """
        randomly deals a card from the deck, removes it from the deck afterwards
        """
        card = random.choice(self.deck)
        self.deck.remove(card)
        print(card)
        return card