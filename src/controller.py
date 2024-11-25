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

    show_message = None 
    message_timer = None

    phand_x = 385
    dhand_x = 385
    
    card_back = pygame.image.load('assets/BACK.png')
    card_back = pygame.transform.scale(card_back, (125, 181.5))

    #deal first player card
    card = deck.deal_card()
    pcards.append((card.load_image(), (phand_x, 350)))
    playerhand += Card.value(card)

    #deal first dealer card
    card = deck.deal_card()
    dcards.append((card.load_image(), (dhand_x, 25)))
    dealerhand += Card.value(card)

    #deal second player card
    card = deck.deal_card()
    pcards.append((card.load_image(), (phand_x, 350)))
    playerhand += Card.value(card)  

    #deal hidden dealer card
    hidden_card = card_back
    
    hidden_card = Card.load_hidden_card(card)

    while self.state == 'GAME':

      current_time = pygame.time.get_ticks()
      self.screen.fill('darkgreen')

      #1. event handler
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        #hit button
        if event.type == pygame.MOUSEBUTTONDOWN:
          if hit.collides(event.pos):
              hand_x += 20
              card = deck.deal_card()
              playerhand += Card.value(card)
              cardimg = card.load_image()
              pcards.append((cardimg, (hand_x, 350)))

      #2 draw cards on screen
      for cardimg, pos in pcards: 
        self.screen.blit(cardimg, pos)
      for cardimg, pos in dcards: 
        self.screen.blit(cardimg, pos)
      self.screen.blit(hidden_card, (dhand_x + 20, 25))

      # UI buttons
      hit = Button((75,75), (300,475), self.screen, 'Hit', (110, 110, 110))
      hit.draw()

      size = Button((0, 0), (500, 560), self.screen, f'{playerhand}', (110, 110, 110))
      size.draw()

      stand = Button((100, 75), (600, 475), self.screen, 'Stand', (110, 110, 110))
      stand.draw()

      #check game logic
      if playerhand == 21 and not show_message:
        show_message = 'Blackjack!'
        message_timer = current_time
      elif playerhand > 21 and not show_message:
        show_message = 'Bust! You Lose'
        message_timer = current_time

      #3 show message for win or lose
      if show_message:
        message_button = Button((0, 0), (500, 300), self.screen, show_message, (110, 110, 110))
        message_button.draw()
       
        if current_time - message_timer > 1500:
          pcards.clear()
          playerhand = 0
          hand_x = 385

          card = deck.deal_card()
          pcards.append((card.load_image(), (hand_x, 350)))
          playerhand += Card.value(card)

          show_message = None
    #3 display next frame
      pygame.display.flip()

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