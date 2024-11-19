import pygame
from card import Card
from player import Player

class Controller:
  
  def __init__(self):
    """
    docstring
    """
    
  def mainloop(self):
    """
    docstring
    """
    while(True):
      #1. Handle Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT():
          pygame.quit()
          exit()
      
      #2 collisions and update models

      #3 redraw next frame

      #4 display next frame
      pygame.display.flip()
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
