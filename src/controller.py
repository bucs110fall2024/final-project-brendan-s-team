import pygame
from src.button import Button
from src.deck import Deck

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

    #game variables
    self.deck = Deck()
    self.deck.make_deck()
    self.playerhand = 0
    self.pcards = []
    self.dealerhand = 0
    self.dcards = []
    self.show_message = None 
    self.message_timer = None
    self.is_stand = False
    self.phand_x = 385
    self.dhand_x = 385
    self.ante = 0
    self.chips = 250

  def initialdeal(self):
    #deal first player card
    card = self.deck.deal_card()
    self.pcards.append((card.load_image(), (self.phand_x, 350)))
    self.playerhand += card.value

    #deal first dealer card
    card = self.deck.deal_card()
    self.dcards.append((card.load_image(), (self.dhand_x, 15)))
    self.dealerhand += card.value

    #deal second player card
    self.phand_x += 20
    card = self.deck.deal_card()
    self.pcards.append((card.load_image(), (self.phand_x, 350)))
    self.playerhand += card.value

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
    """
    loop for the start menu of the game
    """
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
    """
    loop for the main game
    """

    self.initialdeal()

    while self.state == 'GAME':

      if self.deck.deck_size() <= 4:
        self.deck = Deck()
        self.deck.make_deck()

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
              self.phand_x += 20
              card = self.deck.deal_card()
              self.playerhand += card.value
              cardimg = card.load_image()
              self.pcards.append((cardimg, (self.phand_x, 350)))
          if stand.collides(event.pos):
              self.is_stand = True
          if upante.collides(event.pos):
              if self.ante <= 350 and self.chips > self.ante:
                self.ante += 50
          if downante.collides(event.pos):
              if self.ante > 0:
                self.ante -= 50

      #2 draw cards on screen
      for cardimg, pos in self.pcards: 
        self.screen.blit(cardimg, pos)
      for cardimg, pos in self.dcards: 
        self.screen.blit(cardimg, pos)
      self.screen.blit(pygame.transform.scale(pygame.image.load('assets/BACK.png'), (125, 181.5)), (850,200))

      # UI buttons
      hit = Button((75,75), (300,475), self.screen, 'Hit', (110, 110, 110))
      hit.draw()

      stand = Button((100, 75), (600, 475), self.screen, 'Stand', (110, 110, 110))
      stand.draw()

      upante = Button((60,60), (115,480), self.screen, '+50', (110,110,110))
      upante.draw()

      downante = Button((60,60), (45,480), self.screen, '-50', (110,110,110))
      downante.draw()

      #display numbers
      psize = Button((0, 0), (500, 560), self.screen, f'{self.playerhand}', (110, 110, 110))
      psize.draw()

      dsize = Button((0,0), (500, 250), self.screen, f'{self.dealerhand}', (110,110,110))
      dsize.draw()

      antesize = Button((0,0), (112,25), self.screen, f'Ante: {self.ante}', (110,110,110))
      antesize.draw()

      antebar = Button((75,420), (75,50), self.screen, '', 'white')
      antebar.draw()

      chipsdisplay = Button((0,0), (110,565), self.screen, f'Chips: {self.chips}', (110,110,110))
      chipsdisplay.draw()
      
      #ante logic
      if self.ante <= 50:
        antesize = Button((50, self.ante), (87.5, 410), self.screen, '', 'red')
        antesize.draw()
      elif self.ante >= 50:
        antesize = Button((50, self.ante), (87.5, 460 - self.ante), self.screen, '', 'red')
        antesize.draw()
      
      if self.chips < self.ante:
        self.ante = self.chips

      #check game logic
      if not self.show_message:
        if self.is_stand == False:
          if self.playerhand == 21:
            self.show_message = 'Blackjack!'
            self.message_timer = current_time
            self.chips += self.ante * 1.5
          elif self.playerhand > 21:
            self.show_message = 'Bust! You Lose'
            self.message_timer = current_time
            self.chips -= self.ante
        elif self.is_stand == True:
          if self.dealerhand < 17:
            while self.dealerhand < 17:
              self.dhand_x += 20
              card = self.deck.deal_card()
              self.dcards.append((card.load_image(), (self.dhand_x, 15)))
              self.dealerhand += card.value
              self.is_stand = False
          if not self.show_message:
            if self.dealerhand == 21:
              self.show_message = 'Blackjack! You Lose'
              self.message_timer = current_time
              self.chips -= self.ante
            elif self.dealerhand > 21:
              self.show_message = 'Dealer Busts! You Win'
              self.message_timer = current_time
              self.chips += self.ante
            elif self.dealerhand > self.playerhand:
              self.show_message = 'Dealer Wins!'
              self.message_timer = current_time
              self.chips -= self.ante
            elif self.dealerhand < self.playerhand:
              self.show_message = 'You Win!'
              self.message_timer = current_time
              self.chips += self.ante
            elif self.dealerhand == self.playerhand:
              self.show_message = 'Push'
              self.message_timer = current_time

      #3 show message for win or lose
      if self.show_message:
        message_button = Button((0, 0), (500, 300), self.screen, self.show_message, (110, 110, 110))
        message_button.draw()
       
        if current_time - self.message_timer > 1500:
          self.pcards.clear()
          self.playerhand = 0
          self.phand_x = 385

          self.dcards.clear()
          self.dealerhand = 0
          self.dhand_x = 385

          self.initialdeal()

          self.show_message = None
          
    #3 display next frame
      pygame.display.flip()
