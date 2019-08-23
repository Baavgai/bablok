import pygame
# import random
from ..constants import *
from ...constants import BLOCK_NONE
from .game_sprite import GameSprite
from .brick import Brick
from ..colors import COLOR_BG


class Background(GameSprite):
    def __init__(self):
        GameSprite.__init__(self, size=DISPLAY_SIZE)
        self.image.fill(COLOR_BG)
        brick = Brick(BLOCK_NONE)
        xs = [x for x in range(LEFT_WIDTH)]
        xs.extend(range(WELL_WIDTH + LEFT_WIDTH, FULL_WIDTH))
        for y in range(FULL_HEIGHT):
            for x in range(FULL_WIDTH):
                if y < WELL_HEIGHT:
                    if x >= LEFT_WIDTH and x < (WELL_WIDTH + LEFT_WIDTH):
                        continue
                brick.to_pos(x, y).draw(self.image)
