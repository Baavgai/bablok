import pygame
from ..state import GameState
from .constants import EVENT_TICK
# from .. import controller

KB_LOOKUP = {
    GameState.RS_PAUSED: {
        pygame.K_ESCAPE: lambda c: c.unpause_game()
    },
    GameState.RS_DONE: {
    },
    GameState.RS_GAME_OVER: {
        pygame.K_ESCAPE: lambda c: c.restart_game(),
        pygame.K_y: lambda c: c.restart_game(),
        pygame.K_n: lambda c: c.end_game(),
    },
    GameState.RS_PLAYING: {
        pygame.K_KP_PLUS: lambda c: c.level_up(),
        pygame.K_LEFT: lambda c: c.move_left(),
        pygame.K_ESCAPE: lambda c: c.pause_game(),
        pygame.K_RIGHT: lambda c: c.move_right(),
        pygame.K_SPACE: lambda c: c.drop(),
        pygame.K_UP: lambda c: c.rotate(),
        pygame.K_PLUS: lambda c: c.level_up(),
        pygame.K_DOWN: lambda c: c.speed_down(),
    }
}


def update(controller):
    rs = controller.running_state()
    if not rs == GameState.RS_DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.end_game()
            elif event.type == pygame.VIDEORESIZE:
                controller.on_resize(event.size)
            elif event.type == pygame.KEYDOWN:
                lu = KB_LOOKUP[rs]
                if event.key in lu:
                    lu[event.key](controller)
            # elif event.type == pygame.KEYUP and not state.game_over:                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:                    state.entry = GameState.E_NONE
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN and not rs == GameState.RS_GAME_OVER:
                controller.end_speed_down()
            elif event.type == EVENT_TICK and rs == GameState.RS_PLAYING:
                controller.move_down()
    controller.finalize()
