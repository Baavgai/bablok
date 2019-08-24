import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image=None, size=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = None, None
        if image:
            self.image = image
        elif size:
            self.image = pygame.Surface(size)
        if self.image:
            self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
