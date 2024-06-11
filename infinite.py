import pygame
import scene
import player
import zombie
import gemoetry
import random

class Infinite(scene.Scene) :
    def __init__(self, screen: pygame.Surface, gamestatemgr) -> None:
        super().__init__(screen, gamestatemgr)

        self.player = player.Player()
        self.player.rect.x = 400
        
        self.zombie = zombie.Zombie()
        self.zombie.rect.x = 600

        self.ground = gemoetry.rect((0, 0, 0), pygame.Rect(0, 790, 800, 20))

        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        self.entities.add(self.zombie)

        self.geometry = pygame.sprite.Group()
        self.geometry.add(self.ground)

        self.sidescroll_group = pygame.sprite.Group()
        self.sidescroll_group.add(self.player)

        self.clock = pygame.time.Clock()

        self.sidescroll_speed = 35
        self.platform_chance = 4 # percent

    def update(self):
        # Timing
        delta_time = self.clock.get_time() / 1000

        # Background
        self.screen.fill((25, 25, 25))

        # Generating random platforms
       # if random.randint(0, 100) < self.platform_chance :
       #     platform = gemoetry.rect((102, 51, 0), pygame.Rect(random.randint(0,800), random.randint(0, 800), 100, 10))
       #     self.geometry.add(platform)
       #     self.sidescroll_group.add(platform)

        # Drawing Sprites

        self.entities.draw(self.screen)
        self.entities.update()
        #self.zombie.go_to(pygame.Vector2(self.player.rect.x, self.player.rect.y))
        
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

