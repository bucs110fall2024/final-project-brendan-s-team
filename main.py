import pygame
from src.deck import Deck
from src.controller import Controller

def main():
    pygame.init()
    deck = Deck()
    deck.make_deck()
    game = Controller()
    game.mainloop()

if __name__ == '__main__':
    main()
