import pygame
# import random
from ..constants import BLOCK_COUNT, BLOCK_NONE
from .constants import *
from .colors import *


def size_from_brick_size(brick_size):
    return FULL_WIDTH * brick_size, FULL_HEIGHT * brick_size


def to_screen_pos(brick_size, pt):
    x, y = pt
    return x * brick_size, y * brick_size


def bordered_image_for_colors(size, border_width, colors):
    image = pygame.Surface(size)
    w, h = size
    center, top, right, bottom, left = colors
    image.fill(center)
    for i in range(border_width):
        pygame.draw.line(image, top, (i, i), (w - i, i))
        pygame.draw.line(image, left, (i, i), (i, h - i))
        pygame.draw.line(image, right, (w - i, i), (w - i, h - i))
        pygame.draw.line(image, bottom, (i, h - i), (w - i, h - i))
    return image


def color_hsl(h, s, l):
    c = pygame.Color(0, 0, 0)
    c.hsla = (h, s, l)
    return c


def banner_border_image(size):
    colors = [color_hsl(180, 5, x / 2) for x in (50, 70, 35, 20, 60)]
    return bordered_image_for_colors(size, BRICK_BORDER, colors)


def brick_image(block_id, brick_size):
    size = (brick_size, brick_size)
    if block_id == BLOCK_NONE:
        colors = [color_hsl(0, 0, x / 2) for x in (50, 70, 35, 20, 60)]
        return bordered_image_for_colors(size, BRICK_BORDER, colors)
    else:
        hue = [None, COLOR_BLOCK_I, COLOR_BLOCK_O, COLOR_BLOCK_T, COLOR_BLOCK_S, COLOR_BLOCK_Z, COLOR_BLOCK_J, COLOR_BLOCK_L][block_id]
        colors = [color_hsl(hue, 100, x) for x in (50, 70, 35, 20, 60)]
        return bordered_image_for_colors(size, BRICK_BORDER, colors)


def generate_brick_images(brick_size):
    return [brick_image(x, brick_size) for x in range(BLOCK_COUNT)]
