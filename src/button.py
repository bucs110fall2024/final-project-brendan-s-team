import pygame

class Button:
    def __init__(self, size, location, screen, caption, color):
        """
        creates the buttons used on screen
        args:
        size - (x, y)
        location - (x, y)
        screen - the screen button is displayed on
        caption - the text on the button
        color - color of button
        """
        pygame.font.init()
        self.size = size
        self.location = location
        self.color = color
        self.screen = screen
        self.caption = caption
        self.font = pygame.font.SysFont('Impact', 40 , bold=False)
    
    def draw(self):
        """
        draws the button on screen
        """
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.location, self.size), 0, 5)
        caption_surface = self.font.render(self.caption, True, 'white')
        caption_rect = caption_surface.get_rect(center=(self.location[0] + self.size[0] // 2, self.location[1] + self.size[1] // 2))
        self.screen.blit(caption_surface, caption_rect)

    def collides(self, point):
        """
        checks to see if the mouse is over the location of the button to use for clicking events
        args: point - the location of the mouse
        return: returns if the mouse is in the bounds of the button
        """
        x , y = point
        return (self.location[0] <= x <= self.location[0] + self.size[0] and self.location[1] <= y <= self.location[1] + self.size[1])
