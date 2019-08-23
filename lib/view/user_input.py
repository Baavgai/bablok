import pygame
from ..state import GameState
from .constants import EVENT_TICK
# from .. import controller


def update(controller):
    if not controller.is_done():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.end_game()
            elif event.type == pygame.KEYDOWN:
                if controller.is_game_over():
                    if event.key == pygame.K_ESCAPE:
                        controller.restart_game()
                elif controller.is_paused():
                    if event.key == pygame.K_ESCAPE:
                        controller.unpause_game()
                elif event.key == pygame.K_ESCAPE:
                    controller.pause_game()
                elif event.key == pygame.K_LEFT:
                    controller.move_left()
                elif event.key == pygame.K_RIGHT:
                    controller.move_right()
                elif event.key == pygame.K_SPACE:
                    controller.drop()
                elif event.key == pygame.K_UP:
                    controller.rotate()
            # elif event.type == pygame.KEYUP and not state.game_over:                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:                    state.entry = GameState.E_NONE
            elif event.type == EVENT_TICK and controller.is_playing():
                controller.move_down()
    controller.finalize()
