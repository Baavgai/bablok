import pygame
from .sprite.background import Background
from .sprite.banner import Banner
from .sprite.field import Field
from .sprite.score import Score
from .sprite.level import Level
from .sprite.preview import Preview
from . import util
from .constants import EVENT_TICK, FULL_WIDTH, FULL_HEIGHT, LEVEL_TICKS
from ..state import GameState


class Display(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        self.last_level = 0
        self.sprites = pygame.sprite.Group()

        # detector blows, going with fixed size to start  # info = pygame.display.Info()
        self.__init_screen(30)
        # we're always getting a resize hit back when we start up

    def __init_screen(self, brick_size):
        self.brick_size = brick_size
        self.screen = pygame.display.set_mode(util.size_from_brick_size(brick_size), pygame.RESIZABLE)

    def __resize(self):
        self.brick_images = util.generate_brick_images(self.brick_size)
        size = self.screen.get_size()
        self.sprites.empty()
        self.sprites.add(Background(size, self.brick_size, self.brick_images[0]))
        self.sprites.add(Field(self.brick_size, self.brick_images))
        self.sprites.add(Preview(self.brick_size, self.brick_images))
        self.sprites.add(Score(self.brick_size))
        self.sprites.add(Level(self.brick_size))
        self.sprites.add(Banner(size, self.brick_size))

    def on_resize(self, size):
        self.__init_screen(min(size[0] // FULL_WIDTH, size[1] // FULL_HEIGHT))
        self.__resize()

    def update(self, state):
        if not state.level == self.last_level:
            pygame.time.set_timer(EVENT_TICK, LEVEL_TICKS[state.level])
            self.last_level = state.level
        self.sprites.update(state)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def tick(self, state):
        self.clock.tick(60)

    def close(self):
        pygame.quit()
