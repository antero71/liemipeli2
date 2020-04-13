import pygame
from pygame.sprite import Sprite

class Wizard(Sprite):
    """A class to manage the Wizard"""

    def __init__(self, ai_game):
        """Initialize wizard and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the wizard image and get its rect
        self.image = pygame.image.load('pictures/player.png')
        self.rect = self.image.get_rect()

        # Start each new wizard at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the wizard's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the wizard's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.wizard_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.wizard_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.wizard_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.wizard_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_wizard(self):
        """Center the wizard on the sceen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the wizard at its current location."""
        self.screen.blit(self.image,self.rect)

