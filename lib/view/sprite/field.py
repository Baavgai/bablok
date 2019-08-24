import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG
from ...constants import WELL_HEIGHT, WELL_WIDTH
from .game_sprite import GameSprite
from ..util import to_screen_pos


class Field(GameSprite):
    def __init__(self, brick_size, brick_images):
        GameSprite.__init__(self, size=(WELL_WIDTH * brick_size, WELL_HEIGHT * brick_size))
        self.brick_size, self.brick_images = brick_size, brick_images
        x, y = to_screen_pos(self.brick_size, (LEFT_WIDTH, 0))
        self.rect.x = x
        self.rect.y = y

    def update(self, state):
        self.image.fill(COLOR_BG)
        for (pt, block_id) in state.active_grid():
            self.image.blit(self.brick_images[block_id], to_screen_pos(self.brick_size, pt))
