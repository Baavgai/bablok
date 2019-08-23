import pygame
import random
from .state import GameState
from .live_block import pick_block
from .constants import WELL_WIDTH, WELL_HEIGHT, BLOCK_NONE


def crash_block(state, block):
    for (x, y) in block.shape():
        state.grid[y][x] = block.block_id
    state.live_block = None


def winning_rows(state):
    d = {}
    for ((_, y), _) in state.active_grid(False):
        if y in d:
            d[y] += 1
        else:
            d[y] = 1
    return [y for (y, count) in d.items() if count == WELL_WIDTH]


def remove_winning_rows(state):
    rows = winning_rows(state)
    if not rows == []:
        xs = [[BLOCK_NONE for _ in range(WELL_WIDTH)]
              for _ in range(len(rows))]
        xs.extend(row for (i, row) in enumerate(state.grid) if i not in rows)
        state.grid = xs


def can_move(state, block):
    g_blocks = [pt for (pt, _) in state.active_grid(include_live=False)]
    for (x, y) in block.shape():
        if (x, y) in g_blocks:
            return False
        if x < 0 or x >= WELL_WIDTH:
            return False
        elif y >= WELL_HEIGHT:
            return False
    return True


def move_down(state):
    if state.live_block:
        block = state.live_block.move((0, 1))
        if can_move(state, block):
            state.live_block = block
        else:
            crash_block(state, state.live_block)
    # state.move_down = False


def __move_delta(state, delta):
    block = state.live_block.move(delta)
    if can_move(state, block):
        state.live_block = block
    # state.entry = GameState.E_NONE


def move_left(state):
    __move_delta(state, (-1, 0))


def move_right(state):
    __move_delta(state, (1, 0))


def rotate(state):
    block = state.live_block.rotate()
    if can_move(state, block):
        state.live_block = block
    # state.entry = GameState.E_NONE


def drop(state):
    block = state.live_block
    next_block = block.move((0, 1))
    while can_move(state, next_block):
        block = next_block
        next_block = block.move((0, 1))
    crash_block(state, block)
    # state.entry = GameState.E_NONE


def block_eliminate(state):
    # rows = state.winning_rows()
    remove_winning_rows(state)


def spawn_block(state):
    block_eliminate(state)
    state.live_block = state.next_block
    state.next_block = pick_block()
    state.live_block = state.live_block.move((0, 1))
    if not can_move(state, state.live_block):
        state.running_state = GameState.RS_GAME_OVER


def end_game(state):
    state.running_state = GameState.RS_DONE


def restart_game(state):
    state.restart()


def finalize(state):
    if state.running_state == GameState.RS_PLAYING:
        if not state.live_block:
            spawn_block(state)
    return state
