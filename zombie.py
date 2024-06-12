import pygame
import entity
import spritesheet

class Zombie(entity.Entity) :
    def __init__(self) -> None:
        super().__init__()
        self.sheet = spritesheet.SpriteSheet("./Assets/Sprites/Zombie.png")

        self.frames_idle = self.sheet.load_row([32, 32], 0, 8)
        self.frames_walk = self.sheet.load_row([32, 32], 2, 8)
        self.frames_die = self.sheet.load_row([32, 32], 5)
        self.animation_idle = spritesheet.Animation(self.frames_idle, 100)
        self.animation_walk = spritesheet.Animation(self.frames_walk, 100)
        self.animation_die = spritesheet.Animation(self.frames_die, 50)

        self.scale_factor = 3

        self.image = pygame.transform.scale_by(self.frames_idle[0], self.scale_factor)
        self.rect = self.image.get_rect()

        self.animation = self.animation_idle

        # Game logic
        self.health = 100
        self.target : entity.Entity = entity.Entity()
        
    def update(self):
        super().update()
        delta_time = self.clock.get_time() / 1000
        
        # Animation
        if self.velocity.x < 0 :
            self.set_animation(self.animation_walk, True)
        else :
            self.set_animation(self.animation_walk, False)

        self.image = pygame.transform.scale_by(self.animation.animate(delta_time * 1000), self.scale_factor).convert_alpha()
        if self.is_flipped :
            self.image = pygame.transform.flip(self.image, True, False)

        # Follow target (if exists)
        if self.target :
           self.go_towards(pygame.Vector2(self.target.rect.x, self.target.rect.y)) 

        # Update Sprite Coordinates
        self.rect.x += self.velocity.x * delta_time
        self.rect.y += self.velocity.y * delta_time
    
    def go_towards(self, vec2) :
        dir = pygame.Vector2(vec2.x - self.rect.x, vec2.y - self.rect.y).normalize()
        if self.velocity.magnitude() < self.max_walk_speed :
            self.velocity.x += dir.x * self.walk_acceleration

    def set_target(self, ent : entity.Entity) :
        self.target = ent
    

    def die(self) :
        self.set_animation(self.animation_die.on_end(self, lambda : self.kill()))
        self.is_animation_locked = True

    def hurt(self, value) :
        self.health -= value
        if self.health <= 0 :
            self.die()
