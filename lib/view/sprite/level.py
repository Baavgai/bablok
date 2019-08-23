from .msg import Msg
from ...state import GameState


class Level(Msg):
    def __init__(self):
        Msg.__init__(self, 2, Msg.ALIGN_CENTER)

    def _get_message(self, state):
        # if state.running_state == GameState.RS_PAUSED:            return f'Level: {state.level} (paused)'
        return f'Level: {state.level}'
