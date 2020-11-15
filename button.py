"""Module for user made botton class"""
import pygame.font

class Button:
    """Button class to draw a basic play button."""
    def __init__(self, ai_game, msg):
        """
        Initialize button attributes.

        Args:
            ai_game (Class): Alien Invasion Class
            msg ([type]): text to display on button
        """

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.fone = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
            Turn msg into a rendered image and center text on the button.
        Args:
            msg (string): text to display on button.
        """
        self.msg_image = self.fone.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
