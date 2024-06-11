import pygame
import entity
import spritesheet

class Zombie(entity.Entity) :
    def __init__(self) -> None:
        super().__init__()
        self.sheet = spritesheet.SpriteSheet("./Assets/Sprites/Zombie.png")

        self.frames_idle = self.sheet.load_row([32, 32], 0, 8)
        self.frames_die = self.sheet.load_row([32, 32], 5)
        self.animation_idle = spritesheet.Animation(self.frames_idle, 100)
        self.animation_die = spritesheet.Animation(self.frames_die, 50)

        self.scale_factor = 3

        self.image = pygame.transform.scale_by(self.frames_idle[0], self.scale_factor)
        self.rect = self.image.get_rect()

        self.animation = self.animation_idle

        self.health = 100
        
    def update(self):
        super().update()
        delta_time = self.clock.get_time() / 1000
        
        # Animation
        self.image = pygame.transform.scale_by(self.animation.animate(delta_time * 1000), self.scale_factor).convert_alpha()

        # Update Sprite Coordinates
        self.rect.x += self.velocity.x * delta_time
        self.rect.y += self.velocity.y * delta_time
    
    def die(self) :
        self.set_animation(self.animation_die.on_end(self, lambda : self.kill()))


    def hurt(self, value) :
        self.health -= value
        if self.health <= 0 :
            self.die()
