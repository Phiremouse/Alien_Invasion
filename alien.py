""" Creating the Alien Class  """


import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet.
    Args:
        Sprite (class): its a basic sprite.
    """
    def __init__(self, ai_game):
        """ Initalize the alien and set its starting position.
        Args:
            ai_game (Class): Alien Invasion class
        """
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x_pos = float(self.rect.x)
