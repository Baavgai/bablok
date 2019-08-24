import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG, COLOR_FONT
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .msg import Msg
from ..util import to_screen_pos


class Score(Msg):
    def __init__(self, brick_size):
        Msg.__init__(self, brick_size, 5, Msg.ALIGN_RIGHT)

    def _get_message(self, state):
        return f'{state.score} '


"""
Single 	100 x level
Double 	300 x level
Triple 	500 x level
Tetris 	800 x level; difficult
T-Spin no lines (kick) 	100 x level (3-corner T)
0 (3-corner T no kick)
T-Spin no lines (no kick) 	400 x level
T-Spin Single (kick) 	200 x level; difficult (3-corner T)
100 x level, counted as Single (3-corner T no kick)
T-Spin Single (no kick) 	800 x level; difficult
T-Spin Double (kick) 	1200 x level; difficult (3-corner T)
300 x level, counted as Double (3-corner T no kick)
T-Spin Double (no kick) 	1200 x level; difficult
T-Spin Triple 	1600 x level; difficult (3-corner T)
500 x level, counted as Triple (all 3-corner T no kick games and Tetris Zone)
Back to Back difficult line clears 	*3/2
(for example, back to back tetris: 1200 x level)
Combo 	50 x combo count x level (Only available in some games released after Tetris Zone)
Soft drop 	1 point per cell
Hard drop 	2 points per cell 
"""
