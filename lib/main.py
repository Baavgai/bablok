# from .view import user_display, user_input
from .view import user_display, user_input
# from .state import GameState
from .controller import Controller

def main():
    controller = Controller(user_display.Display(), user_input.update)
    while not controller.is_done():
        controller.update_display()
        controller.load_user_input()
        controller.tick()
    controller.close()


if __name__ == "__main__":
    main()
