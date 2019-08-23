import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG
from ...constants import WELL_HEIGHT, WELL_WIDTH
from .game_sprite import GameSprite
from .brick import BRICK_IMAGES, to_screen_pos


class Field(GameSprite):
    def __init__(self):
        GameSprite.__init__(self, size=(WELL_WIDTH * BLOCK_SIZE, WELL_HEIGHT * BLOCK_SIZE))
        x, y = to_screen_pos((LEFT_WIDTH, 0))
        self.rect.x = x
        self.rect.y = y

    def refresh_state(self, state):
        self.image.fill(COLOR_BG)
        for (pt, block_id) in state.active_grid():
            self.image.blit(BRICK_IMAGES[block_id], to_screen_pos(pt))
