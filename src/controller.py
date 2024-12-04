import pygame
from src.button import Button
from src.deck import Deck

class Controller:
  
  def __init__(self):
    """
    inits pygame and the initial screen, state, window caption, and game variables
    args: self
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
    self.has_anted = False
    self.GRAY = (110,110,110)

  def initialdeal(self):
    """
    deals the first cards for the player and dealer
    args: self
    """
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
    args: self
    """
    while True:
      if self.state == 'GAME':
        self.gameloop()
      elif self.state == 'START':
        self.startloop()
      elif self.state == 'LOSE':
        self.loseloop()

  def startloop(self):
    """
    loop for the start menu of the game
    args: self
    """
    while self.state == 'START':
      # Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if playagain.collides(event.pos):
              self.state = 'GAME'

      # redraw next frame
      self.screen.fill('darkgreen')
      playagain = Button((200,100), (400,200), self.screen, 'Play Game', self.GRAY)
      playagain.draw()
      title = Button((0,0), (500,100), self.screen, 'Brendans Blackjack', self.GRAY)
      title.draw()
      
      # display next frame
      pygame.display.flip()

  def loseloop(self):
    """
    loop for the lose menu of the game
    args: self
    """
    while self.state == 'LOSE':
      # event handler
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if playagain.collides(event.pos):
              self.state = 'GAME'
      
      # reset variables on loss
      self.chips = 250
      self.pcards.clear()
      self.playerhand = 0
      self.phand_x = 385
      self.dcards.clear()
      self.dealerhand = 0
      self.dhand_x = 385
      self.show_message = None
      self.has_anted = False

      # redraw next frame
      self.screen.fill('darkgreen')
      playagain = Button((200,100), (400,200), self.screen, 'Play Again', self.GRAY)
      playagain.draw()
      lose = Button((0,0), (490,100), self.screen, 'Out of Chips! You Lose', self.GRAY)
      lose.draw()
      
      # display next frame
      pygame.display.flip()
      
  def gameloop(self):
    """
    loop for the main game
    args: self
    """
    while self.state == 'GAME':

      if self.deck.deck_size() <= 4:
        self.deck = Deck()
        self.deck.make_deck()

      current_time = pygame.time.get_ticks()
      self.screen.fill('darkgreen')

      # event handler
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        # buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.has_anted == False:
            # confirm your ante
            if confirmante.collides(event.pos):
              self.has_anted = True
              self.initialdeal()
            # ante +50
            if upante.collides(event.pos):
                if self.ante <= 350 and self.chips > self.ante:
                  self.ante += 50
            # ante -50
            if downante.collides(event.pos):
                if self.ante > 0:
                  self.ante -= 50
          elif self.has_anted == True:
            # hit
            if hit.collides(event.pos):
                self.phand_x += 20
                card = self.deck.deal_card()
                self.playerhand += card.value
                cardimg = card.load_image()
                self.pcards.append((cardimg, (self.phand_x, 350)))
            # stand
            if stand.collides(event.pos):
                self.is_stand = True

      # draw cards on screen
      for cardimg, pos in self.pcards: 
        self.screen.blit(cardimg, pos)
      for cardimg, pos in self.dcards: 
        self.screen.blit(cardimg, pos)
      
      # draw back of deck
      self.screen.blit(pygame.transform.scale(pygame.image.load('assets/BACK.png'), (125, 181.5)), (850,200))

      # UI buttons
      hit = Button((75,75), (300,475), self.screen, 'Hit', self.GRAY)
      hit.draw()
      stand = Button((100, 75), (600, 475), self.screen, 'Stand', self.GRAY)
      stand.draw()
      upante = Button((60,60), (115,480), self.screen, '+50', self.GRAY)
      upante.draw()
      downante = Button((60,60), (45,480), self.screen, '-50', self.GRAY)
      downante.draw()

      # button to confirm ante if you havent
      if self.has_anted == False:
        confirmante = Button((100,60), (447.5,400), self.screen, 'Ante', self.GRAY)
        confirmante.draw()

      #display numbers
      psize = Button((0, 0), (500, 560), self.screen, f'{self.playerhand}', self.GRAY)
      psize.draw()
      dsize = Button((0,0), (500, 250), self.screen, f'{self.dealerhand}', self.GRAY)
      dsize.draw()
      antesize = Button((0,0), (112,25), self.screen, f'Ante: {self.ante}', self.GRAY)
      antesize.draw()
      antebar = Button((75,420), (75,50), self.screen, '', 'white')
      antebar.draw()
      chipsdisplay = Button((0,0), (110,565), self.screen, f'Chips: {self.chips}', self.GRAY)
      chipsdisplay.draw()
      
      #ante logic
      if self.ante <= 50:
        antesize = Button((50, self.ante), (87.5, 410), self.screen, '', 'red')
        antesize.draw()
      else:
        antesize = Button((50, self.ante), (87.5, 460 - self.ante), self.screen, '', 'red')
        antesize.draw()
      
      # to ensure ante cant be larger than chips
      if self.chips < self.ante:
        self.ante = self.chips
      
      # check if user has no remaining chips
      if self.chips <= 0:
        self.state = 'LOSE'

      #check game logic
      if not self.show_message:
        # check if the player stood, used for player blackjack and bust
        if self.is_stand == False:
          # player blackjack
          if self.playerhand == 21:
            self.show_message = 'Blackjack!'
            self.message_timer = current_time
            self.chips += int(self.ante * 1.5)
          # player bust
          elif self.playerhand > 21:
            self.show_message = 'Bust! You Lose'
            self.message_timer = current_time
            self.chips -= self.ante
        # check if player stood, and finish result of the game
        elif self.is_stand == True:
          # dealer draws until he reaches 17, then stops
          if self.dealerhand < 17:
            while self.dealerhand < 17:
              self.dhand_x += 20
              card = self.deck.deal_card()
              self.dcards.append((card.load_image(), (self.dhand_x, 15)))
              self.dealerhand += card.value
              self.is_stand = False
          # dealer blackjack
          if self.dealerhand == 21:
            self.show_message = 'Blackjack! You Lose'
            self.message_timer = current_time
            self.chips -= self.ante
          # dealer bust
          elif self.dealerhand > 21:
            self.show_message = 'Dealer Busts! You Win'
            self.message_timer = current_time
            self.chips += self.ante
          # dealer win
          elif self.dealerhand > self.playerhand:
            self.show_message = 'Dealer Wins!'
            self.message_timer = current_time
            self.chips -= self.ante
          # player win
          elif self.dealerhand < self.playerhand:
            self.show_message = 'You Win!'
            self.message_timer = current_time
            self.chips += self.ante
          # push
          elif self.dealerhand == self.playerhand:
            self.show_message = 'Push'
            self.message_timer = current_time

      # show message for win or lose
      if self.show_message:
        message_button = Button((0, 0), (500, 300), self.screen, self.show_message, self.GRAY)
        message_button.draw()
       
        if current_time - self.message_timer > 1500:
          self.pcards.clear()
          self.playerhand = 0
          self.phand_x = 385
          self.dcards.clear()
          self.dealerhand = 0
          self.dhand_x = 385
          self.show_message = None
          self.has_anted = False
          
    # display next frame
      pygame.display.flip()