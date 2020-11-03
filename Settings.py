"""Basic Setting class when pygame base surface is called."""
class Settings:
    """A class to store all settiong for Alien Invastion."""
    def __init__(self):
        """initalize the game's setting."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
