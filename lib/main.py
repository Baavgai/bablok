from .view import display, user_input
from .state import GameState


def main():
    display_state = display.init()
    game_state = GameState()
    while game_state.running_state != GameState.RS_DONE:
        display.update(display_state, game_state)
        game_state = user_input.update(game_state)
        display.tick(display_state, game_state)
    display.close()


if __name__ == "__main__":
    main()
