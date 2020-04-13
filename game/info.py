import pygame.font

class Info:
    def __init__(self,ai_game):
        """This class repesent game info message"""
        self.start_message = f"Voit aloittaa pelin {ai_game.settings.game_name} painamalla 'p'. Peli lopetetaan painamalla 'q'."
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.text_color = (40,40,40)
        self.font = pygame.font.SysFont(None,40)

        self.prep_info()


    def prep_info(self):
        """Turn the message into a rendered image."""
        self.info_image = self.font.render(self.start_message, True, self.text_color, self.settings.bg_color)
        self.info_image_rect = self.info_image.get_rect()
        self.info_image_rect.centerx = self.screen_rect.centerx
        self.info_image_rect.top = 20

    def show_start_message(self):
        self.screen.blit(self.info_image, self.info_image_rect)