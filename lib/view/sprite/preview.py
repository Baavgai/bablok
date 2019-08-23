import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .game_sprite import GameSprite
from .brick import BRICK_IMAGES, to_screen_pos


class Preview(GameSprite):
    def __init__(self):
        GameSprite.__init__(self, size=(5 * BLOCK_SIZE, 4 * BLOCK_SIZE))
        # x, y = to_screen_pos((WELL_WIDTH + LEFT_WIDTH + 1, WELL_HEIGHT - 5))
        x, y = to_screen_pos((WELL_WIDTH + LEFT_WIDTH + 1, 8))
        self.rect.x = x
        self.rect.y = y

    def refresh_state(self, state):
        self.image.fill(COLOR_BG)
        blk = state.next_block
        if blk:
            if blk.block_id == BLOCK_I:
                delta = (0.5, 0.5)
            elif blk.block_id == BLOCK_O:
                delta = (1.5, 1)
            else:
                delta = (1, 1)
            for pt in blk.shape_raw_shift(delta):
                self.image.blit(BRICK_IMAGES[blk.block_id], to_screen_pos(pt))
