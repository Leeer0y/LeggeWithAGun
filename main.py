import pygame
import player
import gemoetry
from player import Player

#Init pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

p = Player()

entities_group = pygame.sprite.Group()
entities_group.add(p)

gemoetry_group = pygame.sprite.Group()

g = gemoetry.rect((0, 0, 0), pygame.Rect(0, 790, 800, 20))
gemoetry_group.add(g)

# Gameloop
running = True
while running:
    #limit FPS
    clock.tick(60)

    # Delta time calculations
    delta_time = clock.get_time() / 1000 
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    # Set background
    screen.fill((255, 0, 0))

    entities_group.draw(screen)
    entities_group.update()

    gemoetry_group.draw(screen)

    # Colision
    entity_colisions = pygame.sprite.groupcollide(entities_group, gemoetry_group, False, False)
    if entity_colisions :
        for i in entity_colisions :
            i.set_grounded(True)


    pygame.display.flip()
