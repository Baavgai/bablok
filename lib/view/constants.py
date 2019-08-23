import pygame
from ..constants import WELL_HEIGHT, WELL_WIDTH

BLOCK_SIZE = 24
LEFT_WIDTH = 2
RIGHT_WIDTH = 7
BOTTOM_HEIGHT = 2
FULL_WIDTH = WELL_WIDTH + LEFT_WIDTH + RIGHT_WIDTH
FULL_HEIGHT = WELL_HEIGHT + BOTTOM_HEIGHT
DISPLAY_SIZE = FULL_WIDTH * BLOCK_SIZE, FULL_HEIGHT * BLOCK_SIZE

EVENT_TICK = pygame.USEREVENT + 0
