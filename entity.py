import pygame
import spritesheet

class Entity(pygame.sprite.Sprite):
    def __init__(self, size = (10, 10)) -> None:
        super().__init__()

        # Character
        self.size = size # width, height
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])

        # Flags
        self.is_grounded = False
        self.is_flipped = False
        self.is_animation_locked = False

        # Physics
        self.velocity = pygame.Vector2(0.0, 0.0)
        self.gravity = 9.8
        self.friction = 10

        # Time 
        self.clock = pygame.time.Clock()

        # Movement
        self.max_walk_speed = 100
        self.walk_acceleration = 25
        self.jump_velocity = 200

        # Animation
        self.animation : spritesheet.Animation


    def set_animation(self, animation : spritesheet.Animation, flipped = None) :
        if animation == self.animation and self.is_flipped == flipped :
            return
        if self.is_animation_locked :
            return
        if flipped != None :
            self.is_flipped = flipped

        self.animation = animation
    
    def update(self) :
        
        # gravity
        if self.is_grounded == False:
            self.velocity.y += self.gravity
        else :
            if self.velocity.y > 0.0 :
                self.velocity.y = 0.0
            # friction
            if self.velocity.magnitude() > 0.0 :
                direction_travelling = self.velocity.normalize() # The more velocity in a direction the closer to one this will be in that direction
                if abs(self.velocity.magnitude()) > self.friction :
                    self.velocity -= (direction_travelling * self.friction)
                else :
                    self.velocity = direction_travelling * 0.0
        
        # update clock
        self.clock.tick()

    # Getters / Setters
    def set_grounded(self, value : bool) :
        self.is_grounded = value
    def get_grounded(self) -> bool :
        return self.is_grounded
