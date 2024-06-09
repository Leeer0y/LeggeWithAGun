import pygame
import spritesheet

# TODO
# Make direction a vector, and velocity a scalar quantity


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:

        # Sprite loading and Animations
        self.frames_idle = spritesheet.SpriteSheet("./Assets/Sprites/Skeloton/Skeleton Idle.png").load_all_images((24, 32))
        self.frames_walk = spritesheet.SpriteSheet("./Assets/Sprites/Skeloton/Skeleton Walk.png").load_all_images((22, 33))

        self.animation_idle = spritesheet.Animation(self.frames_idle, 600)
        self.animation_walk = spritesheet.Animation(self.frames_walk, 300)

        self.scale_factor = 2
        
        # Calling parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale_by(self.frames_idle[0], self.scale_factor)

        self.rect = self.image.get_rect()
        
        self.animation = self.animation_idle

        # Flags
        self.is_grounded = False
        self.is_flipped = False

        # Time
        self.clock = pygame.time.Clock()

        # Physics
        self.velocity = pygame.Vector2(0.0, 0.0)
        self.gravity = 9.8
        self.friction = 10 # Changes depending on surface

        # Movement
        self.max_walk_speed = 100.0
        self.walk_acceleration = 25
        self.jump_velocity = 200

        # Animation
        self.walk_animation_threashold = 5

    def set_animation(self, animation : spritesheet.Animation, flipped = None) :
        if animation == self.animation :
            return
        if flipped != None :
            self.is_flipped = flipped
        animation.flipped(self.is_flipped)
        self.animation = animation

    def update(self) :
        # Timing
        self.clock.tick()
        delta_time = self.clock.get_time() / 1000

        # Player Input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] :
            if self.velocity.x < self.max_walk_speed :
                self.velocity.x += self.walk_acceleration
                self.set_animation(self.animation_walk, False)
        if keys[pygame.K_a] :
            if self.velocity.x > (-self.max_walk_speed) :
                self.velocity.x -= self.walk_acceleration
                self.set_animation(self.animation_walk, True)
        if keys[pygame.K_w] :
            if self.is_grounded == True :
                self.is_grounded = False
                self.velocity.y += -(self.jump_velocity)

        # Gravity
        if self.is_grounded == False :
            self.velocity.y += self.gravity
        else :
            if self.velocity.y > 0.0 :
                self.velocity.y = 0.0 
        # Friction
            if self.velocity.magnitude() > 0.0 :
                direction_travelling = self.velocity.normalize() # The higher the velocity in a direction, the closer it will be to 1 
                if abs(self.velocity.magnitude()) > self.friction :
                    self.velocity -= (direction_travelling * self.friction) # Applys friction in direction traveling
                else :
                    self.velocity = direction_travelling * 0

        # Animations
        if abs(self.velocity.x) <= self.walk_animation_threashold :
            self.set_animation(self.animation_idle, None)

        if self.animation == None :
            self.image = pygame.transform.scale_by(self.animation_idle.animate(), self.scale_factor).convert_alpha()
        else :
            self.image = pygame.transform.scale_by(self.animation.animate(), self.scale_factor).convert_alpha()

        # Update Player
        self.rect.x += self.velocity.x * delta_time
        self.rect.y += self.velocity.y * delta_time
       
    # Getters / Setters
    def set_grounded(self, value : bool) :
        self.is_grounded = value
    def get_grounded(self) -> bool :
        return self.is_grounded



