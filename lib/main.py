from .view import user_display, user_input
from .state import GameState


def main():
    display = user_display.Display()
    game_state = GameState()
    while game_state.running_state != GameState.RS_DONE:
        display.update(game_state)
        game_state = user_input.update(game_state)
        display.tick(game_state)
    display.close()


if __name__ == "__main__":
    main()
