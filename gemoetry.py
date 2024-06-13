#############################
# Author: Leo Pearce
# Created: 9/6/24
# Last Edited: 9/6/24
# Description: The geometry class, mainly used for orginisation of ground objects
# In the early days of the game it was going to be a side scroller so it was mainly 
# Used for platforms and ground obsticals, but its no longer as necessary
#############################

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
