import pygame
# import random
from ..constants import *
from .. import colors
from ...constants import WELL_HEIGHT, WELL_WIDTH, BLOCK_I, BLOCK_O
from .game_sprite import GameSprite
from ..util import to_screen_pos, banner_border_image, color_hsl
from ...state import GameState


KEY_COLOR = (0, 0, 128)


class Banner(GameSprite):
    def __init__(self, display_size, brick_size):
        GameSprite.__init__(self, size=display_size)
        self.font = pygame.font.Font(TYPE_FACE, brick_size + brick_size // 2)
        self.sub_font = pygame.font.Font(TYPE_FACE, brick_size)
        # self.sub_font = pygame.font.SysFont(None, brick_size)
        self.last_state = None
        self.image.set_colorkey(KEY_COLOR)
        self.__clear()

    def __clear(self):
        self.image.fill(KEY_COLOR)

    def __add_control(self, xs):
        xs.extend([
            "Controls:",
            "Move - Left and Right",
            "Rotate - Up",
            "Speed Drop - Down",
            "Full Drop - Space",
            "Skip Level - Kbd +"
        ])
        return xs

    def __write_message_texts(self, texts):
        self.__clear()
        gutter = 10
        w = max(x.get_width() for x in texts) + gutter * 2
        h = sum(x.get_height() for x in texts) + (len(texts) + 1) * gutter
        txt_img = banner_border_image((w + BRICK_BORDER * 2, h + BRICK_BORDER * 2))
        r_txt_img = txt_img.get_rect()
        y = gutter + BRICK_BORDER
        for txt in texts:
            txt_img.blit(txt, (txt_img.get_width() // 2 - txt.get_width() // 2, y))
            y += gutter + txt.get_height()
        pos = (self.rect.centerx - txt_img.get_width() // 2, self.rect.centery - (txt_img.get_height() // 1.5))
        self.image.blit(txt_img, pos)

    def __write_messages(self, messages):
        texts = [self.font.render(messages[0], True, colors.COLOR_BANNER_FONT)]
        texts.extend(self.sub_font.render(x, True, colors.COLOR_BANNER_SUBFONT) for x in messages[1:])
        self.__write_message_texts(texts)

    def __build_title(self):
        xs = zip("BaBlok!", [colors.COLOR_BLOCK_I, colors.COLOR_BLOCK_O, colors.COLOR_BLOCK_T, colors.COLOR_BLOCK_S, colors.COLOR_BLOCK_Z, colors.COLOR_BLOCK_J, colors.COLOR_BLOCK_L])
        letters = [self.font.render(letter, True, color_hsl(hue, 100, 50)) for (letter, hue) in xs]
        size = sum(x.get_width() for x in letters), max(x.get_height() for x in letters)
        title_image = pygame.Surface(size)
        title_image.fill(KEY_COLOR)
        title_image.set_colorkey(KEY_COLOR)
        x = 0
        for ch in letters:
            title_image.blit(ch, (x, 0))
            x += ch.get_width()
        return title_image

    def update(self, state):
        if not state.running_state == self.last_state:
            self.last_state = state.running_state
            if state.running_state == GameState.RS_WELCOME:
                texts = [self.__build_title()]
                sub = self.__add_control(["a.k.a Baavgai's Blocks", "Press any key to play"])
                texts.extend(self.sub_font.render(x, True, colors.COLOR_BANNER_SUBFONT) for x in sub)
                self.__write_message_texts(texts)
            elif state.running_state == GameState.RS_PAUSED:
                self.__write_messages(self.__add_control([
                    "PAUSED",
                    "Press ESC to resume"]))
            elif state.running_state == GameState.RS_GAME_OVER:
                self.__write_messages(["GAME OVER", "Play again? (Y/N)"])
            else:
                self.__clear()
