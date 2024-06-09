import pygame
import scene
import player
import gemoetry

class Infinite(scene.Scene) :
    def __init__(self, screen: pygame.Surface, gamestatemgr) -> None:
        super().__init__(screen, gamestatemgr)
        
        self.player = player.Player()
        self.ground = gemoetry.rect((0, 0, 0), pygame.Rect(0, 790, 800, 20))

        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)

        self.geometry = pygame.sprite.Group()
        self.geometry.add(self.ground)

    def update(self):
        # Background
        self.screen.fill((25, 25, 25))

        # Drawing Sprites
        self.entities.draw(self.screen)
        self.entities.update()

        self.geometry.draw(self.screen)

        # Colision
        entity_colisions = pygame.sprite.groupcollide(self.entities, self.geometry, False, False)
        if entity_colisions :
            for i in entity_colisions :
                i.set_grounded(True)

