import pygame
from ..state import GameState
from .constants import EVENT_TICK
from .. import controller


def update(state):
    if state.running_state != GameState.RS_DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.end_game(state)
                return state
            elif event.type == pygame.KEYDOWN:
                if state.running_state == GameState.RS_GAME_OVER:
                    if event.key == pygame.K_ESCAPE:
                        controller.restart_game(state)
                elif event.key == pygame.K_LEFT:
                    controller.move_left(state)
                elif event.key == pygame.K_RIGHT:
                    controller.move_right(state)
                elif event.key == pygame.K_SPACE:
                    controller.drop(state)
                elif event.key == pygame.K_UP:
                    controller.rotate(state)
            # elif event.type == pygame.KEYUP and not state.game_over:                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:                    state.entry = GameState.E_NONE
            elif event.type == EVENT_TICK and state.running_state == GameState.RS_PLAYING:
                controller.move_down(state)
    return controller.finalize(state)
