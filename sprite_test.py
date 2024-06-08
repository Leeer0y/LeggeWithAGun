import pygame
import sprite
from pygame.transform import scale

SCRREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCRREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SpriteSheets')
clock = pygame.time.Clock()

sprite_sheet_image = pygame.image.load('./Assets/Sprites/adventurer_tilesheet.png')

BG = (50, 50, 50)
BLACK = (0, 0, 0)

s = sprite.sheet('./Assets/Sprites/adventurer_tilesheet.png')
s.load_frames((80, 110))

anim1 = sprite.animation([1, 2, 3], 3)
s.add_animation("Test", anim1)

anim2 = sprite.animation([9, 10] , 1000)
s.add_animation("walk", anim2)

running = True
while running:
    #Limit fps
    clock.tick(60)
    delta_time = clock.get_time() / 1000

    #update background
    screen.fill(BG)

    #display image
    s.animate("walk")
    screen.blit(s.frames[s.current_frame], (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
