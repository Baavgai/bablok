import pygame
# import random
from ..constants import *
from ..colors import COLOR_BG, COLOR_BANNER_FONT, COLOR_BANNER_SUBFONT
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .game_sprite import GameSprite
from ..util import to_screen_pos, banner_border_image
from ...state import GameState


KEY_COLOR = (0, 0, 128)


class Banner(GameSprite):
    def __init__(self, display_size, brick_size):
        GameSprite.__init__(self, size=display_size)
        self.font = pygame.font.Font(TYPE_FACE, brick_size + brick_size // 2)
        self.sub_font = pygame.font.Font(TYPE_FACE, brick_size)
        self.last_state = None
        self.image.set_colorkey(KEY_COLOR)
        self.__clear()

    def __clear(self):
        self.image.fill(KEY_COLOR)

    def __write_messages(self, messages):
        self.__clear()
        texts = [self.font.render(messages[0], True, COLOR_BANNER_FONT)]
        texts.extend(self.sub_font.render(x, True, COLOR_BANNER_SUBFONT) for x in messages[1:])
        gutter = 10
        w = max(x.get_width() for x in texts) + gutter * 2
        h = sum(x.get_height() for x in texts) + (len(texts) + 1) * gutter
        txt_img = banner_border_image((w + BRICK_BORDER * 2, h + BRICK_BORDER * 2))
        # txt_img = pygame.Surface((w, h))
        r_txt_img = txt_img.get_rect()
        # txt_img.fill((80, 80, 80))
        y = gutter + BRICK_BORDER
        for txt in texts:
            txt_img.blit(txt, (txt_img.get_width() // 2 - txt.get_width() // 2, y))
            y += gutter + txt.get_height()
        pos = (self.rect.centerx - txt_img.get_width() // 2, self.rect.centery // 2)
        self.image.blit(txt_img, pos)

    def update(self, state):
        if not state.running_state == self.last_state:
            self.last_state = state.running_state
            if state.running_state == GameState.RS_PAUSED:
                self.__write_messages(["PAUSED", "Press ESC to resume"])
            elif state.running_state == GameState.RS_GAME_OVER:
                self.__write_messages(["GAME OVER", "Press ESC to play again"])
            else:
                self.__clear()
