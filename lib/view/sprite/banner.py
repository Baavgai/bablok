import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG, COLOR_BANNER_FONT
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .game_sprite import GameSprite
from .brick import to_screen_pos
from ...state import GameState


KEY_COLOR = (0, 0, 128)


class Banner(GameSprite):
    def __init__(self):
        GameSprite.__init__(self, size=DISPLAY_SIZE)
        self.font = pygame.font.Font(TYPE_FACE, 32)
        # self.font = pygame.font.Font(None, 24)
        self.last_state = None
        self.image.set_colorkey(KEY_COLOR)
        self.__clear()

    def __clear(self):
        self.image.fill(KEY_COLOR)

    def __write_message(self, message):
        self.__clear()
        text = self.font.render(message, True, COLOR_BANNER_FONT, COLOR_BG)
        # r = text.get_rect(center=self.rect.center)
        r = text.get_rect(center=(self.rect.centerx, self.rect.centery // 2))
        self.image.blit(text, r)

    def refresh_state(self, state):
        if not state.running_state == self.last_state:
            self.last_state = state.running_state
            if state.running_state == GameState.RS_PAUSED:
                self.__write_message("PAUSED")
            elif state.running_state == GameState.RS_GAME_OVER:
                self.__write_message("GAME OVER")
            else:
                self.__clear()
