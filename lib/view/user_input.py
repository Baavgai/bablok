import pygame
from ..state import GameState
from .constants import EVENT_TICK
# from .. import controller

KB_LOOKUP = {
    GameState.RS_PAUSED: {
        pygame.K_ESCAPE: lambda c: c.unpause_game()
    },
    GameState.RS_WELCOME: {
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


def __do_keydown(rs, key, controller):
    if rs == GameState.RS_WELCOME:
        controller.start_game()
    else:
        lu = KB_LOOKUP[rs]
        if key in lu:
            lu[key](controller)


def update(controller):
    rs = controller.running_state()
    if not rs == GameState.RS_DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.end_game()
            elif event.type == pygame.VIDEORESIZE:
                controller.on_resize(event.size)
            elif event.type == pygame.KEYDOWN:
                __do_keydown(rs, event.key, controller)
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                controller.end_speed_down()
            elif event.type == EVENT_TICK:
                controller.handle_tick()
    controller.finalize()
