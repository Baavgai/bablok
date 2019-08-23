import pygame
from .sprite.background import Background
from .sprite.banner import Banner
from .sprite.field import Field
from .sprite.score import Score
from .sprite.level import Level
from .sprite.preview import Preview
from .constants import DISPLAY_SIZE, EVENT_TICK
from ..state import GameState


class Display(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.last_level = 0

        self.sprites = pygame.sprite.Group()
        self.sprites.add(Background())
        self.sprites.add(Field())
        self.sprites.add(Preview())
        self.sprites.add(Score())
        self.sprites.add(Level())
        self.sprites.add(Banner())

    def update(self, state):
        if not state.level == self.last_level:
            pygame.time.set_timer(EVENT_TICK, 800)
            self.last_level = state.level
        for x in self.sprites:
            x.refresh_state(state)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def tick(self, state):
        # if state.running_state == GameState.RS_PLAYING:
        self.clock.tick(60)

    def close(self):
        pygame.quit()
