class GameStats:
    """Track statistics for Wizard Broth."""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.more_info = False
        self.show_inventory = False
