import pygame
# import random
from ...constants import BLOCK_COUNT, BLOCK_NONE
from ..constants import *
from ..colors import *
from .game_sprite import GameSprite


def to_screen_pos(pt):
    x, y = pt
    return x * BLOCK_SIZE, y * BLOCK_SIZE


def brick_image(block_id):
    image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
    rect = image.get_rect()
    color, color_top, color_r, color_bottom, color_l = [COLOR_BLOCK_NONE, COLOR_BLOCK_I, COLOR_BLOCK_O, COLOR_BLOCK_T, COLOR_BLOCK_S, COLOR_BLOCK_Z, COLOR_BLOCK_J, COLOR_BLOCK_L][block_id]
    image.fill(color)
    for i in range(5):
        sz = BLOCK_SIZE - i
        if color_top:
            pygame.draw.line(image, color_top, (i, i), (sz, i))
        if color_l:
            pygame.draw.line(image, color_l, (i, i), (i, sz))
        if color_r:
            pygame.draw.line(image, color_r, (sz, i), (sz, sz))
        if color_bottom:
            pygame.draw.line(image, color_bottom, (i, sz), (sz, sz))
    # pygame.draw.rect(image, COLOR_BG, rect, 1)
    return image


BRICK_IMAGES = [brick_image(x) for x in range(BLOCK_COUNT)]


class Brick(GameSprite):
    def __init__(self, block_id):
        GameSprite.__init__(self, image=BRICK_IMAGES[block_id])
        self.block_id = block_id

    def to_pos(self, vx, vy):
        x, y = to_screen_pos((vx, vy))
        self.rect.x = x
        self.rect.y = y
        return self
