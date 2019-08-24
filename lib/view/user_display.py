import pygame
from .sprite.background import Background
from .sprite.banner import Banner
from .sprite.field import Field
from .sprite.score import Score
from .sprite.level import Level
from .sprite.preview import Preview
from . import util
from .constants import EVENT_TICK, FULL_WIDTH, FULL_HEIGHT
from ..state import GameState

import os


def size_from_brick_size(brick_size):
    return FULL_WIDTH * brick_size, FULL_HEIGHT * brick_size

# pygame.set_icon(Surface)


class Display(object):
    def __init__(self):
        self.clock = pygame.time.Clock()

        pygame.init()

        self.last_level = 0
        self.sprites = pygame.sprite.Group()

        # detector blows, going with fixed size to start
        # info = pygame.display.Info()
        brick_size = 30

        self.screen = pygame.display.set_mode(size_from_brick_size(brick_size), pygame.RESIZABLE)
        # we're always getting a resize hit back when we start up

    def __resize(self):
        self.brick_images = util.generate_brick_images(self.brick_size)
        size = self.screen.get_size()

        self.sprites.empty()
        self.sprites.add(Background(size, self.brick_size, self.brick_images[0]))
        self.sprites.add(Field(self.brick_size, self.brick_images))
        self.sprites.add(Preview(self.brick_size, self.brick_images))
        self.sprites.add(Score(self.brick_size))
        self.sprites.add(Level(self.brick_size))
        self.sprites.add(Banner(size))

    def on_resize(self, size):
        screen_x, screen_y = size
        self.brick_size = min(screen_x // FULL_WIDTH, screen_y // FULL_HEIGHT)
        # print(size, self.brick_size, size_from_brick_size(self.brick_size))
        self.screen = pygame.display.set_mode(size_from_brick_size(self.brick_size), pygame.RESIZABLE)
        self.__resize()

    def update(self, state):
        if not state.level == self.last_level:
            pygame.time.set_timer(EVENT_TICK, [None, 800, 700, 600, 500, 400, 300, 150, 100, 75][state.level])
            # (11 - state.level) * 100)
            self.last_level = state.level
        # for x in self.sprites:            x.refresh_state(state)
        self.sprites.update(state)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def tick(self, state):
        # if state.running_state == GameState.RS_PLAYING:
        self.clock.tick(60)

    def close(self):
        pygame.quit()
