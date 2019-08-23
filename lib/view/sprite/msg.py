import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG, COLOR_FONT
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .game_sprite import GameSprite
from .brick import to_screen_pos


class Msg(GameSprite):
    def __init__(self, row):
        GameSprite.__init__(self, size=(5 * BLOCK_SIZE, BLOCK_SIZE))
        x, y = to_screen_pos((WELL_WIDTH + LEFT_WIDTH + 1, row))
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font("freesansbold.ttf", BLOCK_SIZE - 4)

    def _get_message(self, state):
        return ""

    def refresh_state(self, state):
        self.image.fill(COLOR_BG)
        text = self.font.render(self._get_message(state), True, COLOR_FONT)
        self.image.blit(text, (2, 2))
