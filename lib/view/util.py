import pygame
# import random
from ..constants import BLOCK_COUNT, BLOCK_NONE
from .constants import *
from .colors import *


def to_screen_pos(brick_size, pt):
    x, y = pt
    return x * brick_size, y * brick_size


def brick_image(block_id, brick_size):
    image = pygame.Surface((brick_size, brick_size))
    rect = image.get_rect()
    color, color_top, color_r, color_bottom, color_l = [COLOR_BLOCK_NONE, COLOR_BLOCK_I, COLOR_BLOCK_O, COLOR_BLOCK_T, COLOR_BLOCK_S, COLOR_BLOCK_Z, COLOR_BLOCK_J, COLOR_BLOCK_L][block_id]
    image.fill(color)
    for i in range(5):
        sz = brick_size - i
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


def generate_brick_images(brick_size):
    return [brick_image(x, brick_size) for x in range(BLOCK_COUNT)]
