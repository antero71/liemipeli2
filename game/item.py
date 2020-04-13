import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    """A class represent an item on the world."""
    def __init__(self,ai_game,item_type):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        if item_type == 0:
            self.image = pygame.image.load('pictures/mushroom.bmp')
        elif item_type == 1:
            self.image = pygame.image.load('pictures/dragon.png')
        elif item_type == 2:
            self.image = pygame.image.load('pictures/fish.png')

        self.rect = self.image.get_rect()

        # Start each new item near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the wizard at its current location."""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """Return True if item is at edge of sceen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
