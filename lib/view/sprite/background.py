import pygame
# import random
from ..constants import *
from ...constants import BLOCK_NONE
from .game_sprite import GameSprite
from ..util import to_screen_pos
from ..colors import COLOR_BG


class Background(GameSprite):
    def __init__(self, display_size, brick_size, bg_brick_image):
        GameSprite.__init__(self, size=display_size)
        self.image.fill(COLOR_BG)
        xs = [x for x in range(LEFT_WIDTH)]
        xs.extend(range(WELL_WIDTH + LEFT_WIDTH, FULL_WIDTH))
        for y in range(FULL_HEIGHT):
            for x in range(FULL_WIDTH):
                if y < WELL_HEIGHT:
                    if x >= LEFT_WIDTH and x < (WELL_WIDTH + LEFT_WIDTH):
                        continue
                self.image.blit(bg_brick_image, to_screen_pos(brick_size, (x, y)))
