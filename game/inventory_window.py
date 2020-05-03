import pygame.font
from pygame.sprite import Group

class InventoryWindow():

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ai_game.settings

        # Font settings for scoring informaton.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)

        # Inventory
        self.inventory = ai_game.inventory

        self.prep_inventory()

    def prep_inventory(self):
        """Turn the high score into a rendered image."""
        #high_score = round(self.stats.high_score, -1)
        inventory_items_str = f"{self.inventory.items}"
        self.inventory_items_image = self.font.render(inventory_items_str, True, self.text_color, self.settings.bg_color)
        # Center the high score at the top of the screen.
        self.inventory_items_rect = self.inventory_items_image.get_rect()
        self.inventory_items_rect.right = self.screen_rect.right - 20
        self.inventory_items_rect.top = 40 # self.score_rect.top

    def show_inventory(self):
        self.screen.blit(self.inventory_items_image,self.inventory_items_rect)