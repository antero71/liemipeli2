class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""

        # Screen settings
        # 1200,800 was default
        self.screen_width = 1200
        self.screen_height = 800

        self.bg_color = (86, 205, 110)

        # Wizard settings
        self.wizard_speed = 3