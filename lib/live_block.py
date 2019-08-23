import pygame
import random
from .constants import *


def point_add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])


class LiveBlock(object):
    def __init__(self, block_id, pattern, pos=None):
        self.block_id = block_id
        self.pattern = [x for x in pattern]
        if pos:
            self.pos = pos
        else:
            self.pos = ((WELL_WIDTH // 2), -1)

    def move(self, delta):
        return LiveBlock(self.block_id, self.pattern, point_add(self.pos, delta))

    def rotate(self):
        sz = len(self.pattern)
        # pattern = [[self.pattern[sz - 1 - x][y] for x in range(sz)] for y in range(sz)]
        pattern = [[self.pattern[x][sz - 1 - y] for x in range(sz)] for y in range(sz)]
        return LiveBlock(self.block_id, pattern, self.pos)

    def shape_raw(self):
        sz = len(self.pattern)
        return (pt for (pt, live) in (((x, y), self.pattern[y][x]) for x in range(sz) for y in range(sz)) if live == 1)

    def shape_raw_shift(self, pos):
        return [point_add(p, pos) for p in self.shape_raw()]

    def shape(self):
        return self.shape_raw_shift(self.pos)

# BLOCK_NONE, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_S, BLOCK_Z, BLOCK_J, BLOCK_L, BLOCK_COUNT = range(9)


PATTERNS = [
    #  BLOCK_I
    [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    #  BLOCK_O
    [
        [1, 1],
        [1, 1]
    ],
    # BLOCK_T
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    # BLOCK_S
    [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ],
    # BLOCK_Z
    [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    # BLOCK_J
    [
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    # BLOCK_L
    [
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ],
]


def pick_block():
    block_id = random.randint(1, BLOCK_COUNT - 1)
    return LiveBlock(block_id, PATTERNS[block_id - 1])

# def pick_block():    return LiveBlock(BLOCK_I, PATTERNS[BLOCK_I - 1])
