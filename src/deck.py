from src.card import Card
#import random

class Deck:
    def __init__(self, deck=0):
        self.deck = deck
    
    def make_deck(self):
        suits = ['H', 'D', 'C', 'S']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        deck = []
        for suit in suits:
            for rank, value in zip(ranks, values):
                card = Card(suit, rank, value) 
                deck.append(card) 
        print(deck)
