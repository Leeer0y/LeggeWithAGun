import pygame
import player
from player import Player

#Init pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

p = Player()
p.position = pygame.Vector2(400, 0)

ground = pygame.Rect(0, 700, 800, 10)

colision_list = [ground]

# Gameloop
running = True
while running:
    #limit FPS
    clock.tick(60)

    # Delta time calculations
    delta_time = clock.get_time() / 1000 
    
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

   
    #Set background
    screen.fill((255, 0, 0))

    p.render(screen, delta_time, colision_list)
    pygame.draw.rect(screen, (155, 155, 155), ground)

    pygame.display.flip()
