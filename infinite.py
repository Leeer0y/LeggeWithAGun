import pygame
import scene
import player
import gemoetry

class Infinite(scene.Scene) :
    def __init__(self, screen: pygame.Surface, gamestatemgr) -> None:
        super().__init__(screen, gamestatemgr)

        self.player = player.Player()
        self.player.rect.x = 400

        self.ground = gemoetry.rect((0, 0, 0), pygame.Rect(0, 790, 800, 20))

        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)

        self.geometry = pygame.sprite.Group()
        self.geometry.add(self.ground)

        self.sidescroll_group = pygame.sprite.Group()
        self.sidescroll_group.add(self.player)

        self.sidescroll_speed = 35

        self.clock = pygame.time.Clock()

    def update(self):
        # Timing
        delta_time = self.clock.get_time() / 1000

        # Background
        self.screen.fill((25, 25, 25))

        # Drawing Sprites
        self.entities.draw(self.screen)
        self.entities.update()

        self.geometry.draw(self.screen)

        # Side sidescroll_group
        for i in self.sidescroll_group.sprites() :
            i.rect.x -= self.sidescroll_speed * delta_time

        # Colision
        entity_colisions = pygame.sprite.groupcollide(self.entities, self.geometry, False, False)
        if entity_colisions :
            for i in entity_colisions :
                i.set_grounded(True)

        self.clock.tick()

