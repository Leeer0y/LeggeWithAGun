import pygame
from pygame.key import get_mods

class Geometry(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        
        # Geometry

class rect(Geometry):
    def __init__(self, colour, rect : pygame.Rect) -> None:
        super().__init__()
        self.image = pygame.Surface([rect.width, rect.height])
        self.image.fill(colour)

        pygame.draw.rect(self.image, colour, rect)

        self.rect = self.image.get_rect()
        self.rect.top = rect.top
        self.rect.left = rect.left
