import pygame
from src.button import Button
from src.deck import Deck
from src.card import Card
# from player import Player

class Controller:
  
  def __init__(self):
    """
    inits pygame and the initial screen, state, and window caption
    """
    pygame.init()
    pygame.event.pump()

    self.screen = pygame.display.set_mode((1000, 600))
    self.state = 'START'
    self.caption = pygame.display.set_caption('Blackjack')
    
  def mainloop(self):
    """
    calls the loops for each respective state
    """
    while True:
      if self.state == 'GAME':
        self.gameloop()
      elif self.state == 'START':
        self.startloop()
      elif self.state == 'END':
        self.endloop()

  def startloop(self):
    while self.state == 'START':
      #1. Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if playagain.collides(event.pos):
              self.state = 'GAME'
      
      #2 collisions and update models

      #3 redraw next frame
      self.screen.fill('darkgreen')
      playagain = Button((200,100), (400,200), self.screen, 'Play Game', (110,110,110))
      playagain.draw()
      
      #4 display next frame
      pygame.display.flip()
      
  def gameloop(self):

    deck = Deck()
    deck.make_deck()

    playerhand = 0
    pcards = []
    dealerhand = 0
    dcards = []

    hand_x = 375

    card = deck.deal_card()
    pcards.append((card.load_image(), (hand_x, 350)))
    playerhand += Card.value(card)

    while self.state == 'GAME':
      self.screen.fill('darkgreen')

      #1. event handler
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        #hit button
        if event.type == pygame.MOUSEBUTTONDOWN:
          if hit.collides(event.pos):
              hand_x += 25
              card = deck.deal_card()
              playerhand += Card.value(card)
              cardimg = card.load_image()
              pcards.append((cardimg, (hand_x, 350)))

      #2 update game logic

      #2 redraw next frame
      for cardimg, pos in pcards: 
        self.screen.blit(cardimg, pos)
      # UI buttons
      hit = Button((75,75), (300,475), self.screen, 'Hit', (110, 110, 110))
      hit.draw()

      size = Button((0, 0), (500, 560), self.screen, f'{playerhand}', (110, 110, 110))
      size.draw()

      stand = Button((100, 75), (600, 475), self.screen, 'Stand', (110, 110, 110))
      stand.draw()

      #3 display next frame
      pygame.display.flip()

      #4 update game logic
      if playerhand == 21:
        show_message = 'Blackjack!'
        playerhand = 0
        hand_x = 375
      elif playerhand > 21:
        show_message = 'Bust! You Lose'
        playerhand = 0
        hand_x = 375
      
      if show_message():
       message_button = Button((0, 0), (500, 300), self.screen, show_message, (110, 110, 110)) 
       message_button.draw() 
       pygame.display.flip() 
       pygame.time.wait(1000) 
       pcards.clear() 
       show_message = None



  def endloop(self):
    while self.state == 'END':
      #1. Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      
      #2 collisions and update models

      #3 redraw next frame
      self.screen.fill('darkgreen')
      #4 display next frame
      pygame.display.flip()
  
  def game_logic(self, playerhand):
      if playerhand == 21:
        blackjack = Button((0,0), (500,300), self.screen, 'BlackJack!', (110,110,110))
        blackjack.draw()
        # pcards.clear()
        # playerhand = 0
        # hand_x = 375
      elif playerhand > 21:
        pbust = Button((0,0), (500,300), self.screen, 'Bust! You Lose', (110,110,110))
        pbust.draw()