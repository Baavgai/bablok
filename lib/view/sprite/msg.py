import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG, COLOR_FONT
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .game_sprite import GameSprite
from .brick import to_screen_pos


class Msg(GameSprite):
    ALIGN_LEFT, ALIGN_CENTER, ALIGN_RIGHT = range(3)

    def __init__(self, row, align=None):
        GameSprite.__init__(self, size=(5 * BLOCK_SIZE, BLOCK_SIZE))
        if align:
            self.align = align
        else:
            self.align = Msg.ALIGN_LEFT
        x, y = to_screen_pos((WELL_WIDTH + LEFT_WIDTH + 1, row))
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font(TYPE_FACE, BLOCK_SIZE - 4)

    def _get_message(self, state):
        return ""

    def refresh_state(self, state):
        self.image.fill(COLOR_BG)
        text = self.font.render(self._get_message(state), True, COLOR_FONT)
        if self.align == Msg.ALIGN_RIGHT:
            x = self.image.get_width() - text.get_width() - 2
        elif self.align == Msg.ALIGN_CENTER:
            x = self.image.get_width() // 2 - text.get_width() // 2
        else:
            x = 2
        self.image.blit(text, (x, 2))
