import pygame
from .sprite.background import Background
from .sprite.field import Field
from .sprite.preview import Preview
from .constants import DISPLAY_SIZE, EVENT_TICK
from ..state import GameState


class DisplayState(object):
    def __init__(self):
        self.background = Background()
        self.field = Field()
        self.preview = Preview()

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.background)
        self.sprites.add(self.field)
        self.sprites.add(self.preview)

    def refresh_state(self, state):
        for x in (self.field, self.preview):
            x.refresh_state(state)

    def draw(self, screen):
        self.sprites.draw(screen)

    def update(self, screen, state):
        self.refresh_state(state)
        self.draw(screen)
        pygame.display.flip()


DISPLAY = DisplayState()


def init():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.time.set_timer(EVENT_TICK, 800)
    return screen, clock


def update(display_state, game_state):
    screen, clock = display_state
    DISPLAY.update(screen, game_state)


def tick(display_state, game_state):
    # if state.running_state == GameState.RS_PLAYING:
    screen, clock = display_state
    clock.tick(60)


def close():
    pygame.quit()
