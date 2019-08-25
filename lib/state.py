from .constants import WELL_WIDTH, WELL_HEIGHT, BLOCK_NONE
from .live_block import pick_block


class GameState(object):
    RS_PLAYING, RS_DONE, RS_GAME_OVER, RS_PAUSED = range(4)
    MAX_LEVEL = 9

    def __init__(self):
        self.running_state = GameState.RS_PLAYING
        self.grid = [[BLOCK_NONE for _ in range(WELL_WIDTH)] for _ in range(WELL_HEIGHT)]
        self.live_block = None
        self.next_block = pick_block()
        self.score = 0
        self.level = 1
        self.lines_until_next_level = 10
        self.speed_down = False

    def active_grid(self, include_live=True):
        xs = [((x, y), self.grid[y][x]) for y in range(WELL_HEIGHT) for x in range(WELL_WIDTH) if self.grid[y][x] != BLOCK_NONE]
        if include_live and self.live_block:
            xs.extend((pt, self.live_block.block_id) for pt in self.live_block.shape())
        return xs
