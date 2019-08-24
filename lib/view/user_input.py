import pygame
from ..state import GameState
from .constants import EVENT_TICK
# from .. import controller

KB_LOOKUP = {
    pygame.K_KP_PLUS: lambda c: c.level_up(),
    pygame.K_LEFT: lambda c: c.move_left(),
    pygame.K_ESCAPE: lambda c: c.pause_game(),
    pygame.K_RIGHT: lambda c: c.move_right(),
    pygame.K_SPACE: lambda c: c.drop(),
    pygame.K_UP: lambda c: c.rotate(),
    pygame.K_PLUS: lambda c: c.level_up(),
    pygame.K_DOWN: lambda c: c.speed_down(),
}


def update(controller):
    if not controller.is_done():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.end_game()
            elif event.type == pygame.VIDEORESIZE:
                controller.on_resize(event.size)
            elif event.type == pygame.KEYDOWN:
                if controller.is_game_over():
                    if event.key == pygame.K_ESCAPE:
                        controller.restart_game()
                elif controller.is_paused():
                    if event.key == pygame.K_ESCAPE:
                        controller.unpause_game()
                elif event.key in KB_LOOKUP:
                    KB_LOOKUP[event.key](controller)
            # elif event.type == pygame.KEYUP and not state.game_over:                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:                    state.entry = GameState.E_NONE
            elif event.type == pygame.KEYUP and pygame.K_DOWN and not controller.is_game_over():
                controller.end_speed_down()
            elif event.type == EVENT_TICK and controller.is_playing():
                controller.move_down()
    controller.finalize()
