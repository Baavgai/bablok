import pygame
# import random
from ..constants import BLOCK_COUNT, BLOCK_NONE
from .constants import *
from .colors import *


def to_screen_pos(brick_size, pt):
    x, y = pt
    return x * brick_size, y * brick_size


def bordered_image_for_colors(size, border_width, colors):
    image = pygame.Surface(size)
    w, h = size
    center, top, left, bottom, right = colors
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


def for_lum(c, l):
    h, s = c.hsla[0], c.hsla[1]
    return color_hsl(h, s, l)


def bordered_image(ctrml_lum, size, color, border_width):
    c = pygame.Color(*color)
    colors = [for_lum(c, l) for l in ctrml_lum]
    print([x.hsla for x in colors])
    return bordered_image_for_colors(size, border_width, colors)


def brick_image(block_id, brick_size):
    border_width = 5
    size = (brick_size, brick_size)
    color = [COLOR_BLOCK_NONE, COLOR_BLOCK_I, COLOR_BLOCK_O, COLOR_BLOCK_T, COLOR_BLOCK_S, COLOR_BLOCK_Z, COLOR_BLOCK_J, COLOR_BLOCK_L][block_id][0]
    if block_id == BLOCK_NONE:
        colors = [color_hsl(0, 0, x // 2) for x in (50, 70, 33, 24, 60)]
        return bordered_image_for_colors(size, border_width, colors)
    else:
        return bordered_image((50, 70, 33, 24, 60), size, color, border_width)


def brick_image2(block_id, brick_size):
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
