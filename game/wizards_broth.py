import sys
import pygame

from settings import Settings
from game_stats import GameStats
from wizard import Wizard
from info import Info
from item import Item

class WizardsBroth:
    """Overal class to manage game assist and behavior"""

    def __init__(self):
        pygame.init()

        self.settings = Settings(self)

        self.screen = pygame.display.set_mode((0, 0),
                                              pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption(self.settings.game_name)
        self.wizard = Wizard(self)

        # Create an instance to game statistics
        self.stats = GameStats(self)
        self.info = Info(self)
        self.item = Item(self,1)

        # Set the background color.
        self.bg_color=(150,230,150)

    def _check_events(self):
        # Watch for keyboard and mouse events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print("next write high score")
                #self._write_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = False
        elif event.key == pygame.K_UP:
            self.wizard.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.wizard.moving_down = False

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.wizard.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.wizard.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_o:
            self.stats.more_info = True
        elif event.key == pygame.K_ESCAPE:
            self.stats.more_info = False
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                #self._reset_and_start_game()
                self.stats.game_active = True

    def __update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.wizard.blitme()
        self.item.blitme()

        if not self.stats.game_active and not self.stats.more_info:
            self.info.show_message(self.settings.start_message)

        if self.stats.more_info:
            self.info.show_message(self.settings.instructions)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.wizard.update()

            self.__update_screen()

if __name__ == '__main__':
    ai = WizardsBroth()
    ai.run_game()

