class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize the game's static settings"""
        self.ai_game = ai_game
        # Screen settings
        # 1200,800 was default
        self.screen_width = 1200
        self.screen_height = 800

        self.bg_color = (86, 205, 110)

        # Wizard settings
        self.wizard_speed = 3

        self.game_name = 'Liemipeli'
        self.start_message = f"Voit aloittaa pelin {self.game_name} painamalla 'p'. Peli lopetetaan painamalla 'q'. Lisätietoa saat painamalla 'o'"
        self.instructions = f"Ohjaa Velhoa nuolinäppäimillä, kun kohtaat esineen, voit poimia sen painamalla välilyönti-näppäintä."