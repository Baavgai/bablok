import pygame
import random
from .state import GameState
from .live_block import pick_block
from .constants import WELL_WIDTH, WELL_HEIGHT, BLOCK_NONE


class Controller(object):
    def __init__(self, display, user_input):
        self.display = display
        self.user_input = user_input
        self.state = GameState()

    def is_done(self):
        return self.state.running_state == GameState.RS_DONE

    def is_playing(self):
        return self.state.running_state == GameState.RS_PLAYING

    def is_paused(self):
        return self.state.running_state == GameState.RS_PAUSED

    def is_game_over(self):
        return self.state.running_state == GameState.RS_GAME_OVER

    def update_display(self):
        self.display.update(self.state)

    def load_user_input(self):
        self.user_input(self)

    def tick(self):
        self.display.tick(self.state)

    def close(self):
        self.display.close()

    def end_game(self):
        self.state.running_state = GameState.RS_DONE

    def pause_game(self):
        self.state.running_state = GameState.RS_PAUSED

    def unpause_game(self):
        self.state.running_state = GameState.RS_PLAYING

    def restart_game(self):
        self.state = GameState()

    def __can_move(self, block):
        g_blocks = [pt for (pt, _) in self.state.active_grid(include_live=False)]
        for (x, y) in block.shape():
            if (x, y) in g_blocks:
                return False
            if x < 0 or x >= WELL_WIDTH:
                return False
            elif y >= WELL_HEIGHT:
                return False
        return True

    def __move_delta(self, delta):
        if self.state.live_block:
            block = self.state.live_block.move(delta)
            if self.__can_move(block):
                self.state.live_block = block

    def move_left(self):
        self.__move_delta((-1, 0))

    def move_right(self):
        self.__move_delta((1, 0))

    def rotate(self):
        if self.state.live_block:
            block = self.state.live_block.rotate()
            if self.__can_move(block):
                self.state.live_block = block

    def __crash_block(self, block):
        for (x, y) in block.shape():
            self.state.grid[y][x] = block.block_id
        self.state.live_block = None

    def drop(self):
        block = self.state.live_block
        next_block = block.move((0, 1))
        while self.__can_move(next_block):
            self.state.score += 2
            block = next_block
            next_block = block.move((0, 1))
        self.__crash_block(block)
        # state.entry = GameState.E_NONE

    def move_down(self):
        if self.state.live_block:
            block = self.state.live_block.move((0, 1))
            if self.__can_move(block):
                self.state.live_block = block
                self.state.score += 1
                return True
            else:
                self.__crash_block(self.state.live_block)
        return False

    def __remove_winning_rows(self):
        d = {}
        for ((_, y), _) in self.state.active_grid(False):
            if y in d:
                d[y] += 1
            else:
                d[y] = 1
        rows = [y for (y, count) in d.items() if count == WELL_WIDTH]
        ct = len(rows)
        if ct > 0:
            xs = [[BLOCK_NONE for _ in range(WELL_WIDTH)]
                  for _ in range(len(rows))]
            xs.extend(row for (i, row) in enumerate(self.state.grid) if i not in rows)
            self.state.grid = xs
            self.state.score += [0, 100, 300, 500, 800][ct] * self.state.level

    def __spawn_block(self):
        self.__remove_winning_rows()
        self.state.live_block = self.state.next_block
        self.state.next_block = pick_block()
        self.state.live_block = self.state.live_block.move((0, 1))
        if not self.__can_move(self.state.live_block):
            self.state.running_state = GameState.RS_GAME_OVER

    def finalize(self):
        if self.state.running_state == GameState.RS_PLAYING:
            if not self.state.live_block:
                self.__spawn_block()
                self.state.speed_down = False
            elif self.state.speed_down:
                self.speed_down()

    def level_up(self):
        if self.state.level < 9:
            self.state.level += 1

    def speed_down(self):
        if self.move_down():
            self.state.speed_down = True
            self.state.score += 1
        else:
            self.state.speed_down = False


    def end_speed_down(self):
        self.state.speed_down = False

