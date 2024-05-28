import pygame
import player
from player import Player

#Init pygame
pygame.init()


screen = pygame.display.set_mode((800, 800))

p = Player()
p.position = pygame.Vector2(400, 0)

ground = pygame.Rect(0, 700, 800, 10)

colision_list = [ground]
last_frame_ticks = pygame.time.get_ticks()

# Gameloop
running = True
while running:

    # Delta time calculations
    t = pygame.time.get_ticks()
    delta_time = (t - last_frame_ticks) / 1000.0
    last_frame_ticks = t
    
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

        p.player_controls(event, delta_time)
   
    #Set background
    screen.fill((255, 0, 0))

    p.render(screen, delta_time)
    pygame.draw.rect(screen, (155, 155, 155), ground)

    # Player Gravity
    #if p.hitbox.collidelist(colision_list) >= 0 :
     #   p.isGrounded = True

    pygame.display.flip()
