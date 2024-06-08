import pygame
import spritesheet

# TODO
# Make direction a vector, and velocity a scalar quantity

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        # Calling parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.frames = spritesheet.SpriteSheet("./Assets/Sprites/adventurer_tilesheet.png").load_all_images((80, 110))
        self.image = pygame.Surface([80, 110]).convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.image = self.frames[0]

        self.rect = self.image.get_rect()

        # Flags
        self.is_grounded = False

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

        # Animations
        self.annimation = None
        self.sprite_flipped = False
        self.walk_animation_threashold = 5 # the speed when the walk animation wont play
        self.walk_animation = spritesheet.animation([9, 11], 200)

                         
    def update(self) :
        # Timing
        self.clock.tick()
        delta_time = self.clock.get_time() / 1000

        # Player Input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] :
            if self.velocity.x < self.max_walk_speed :
                self.velocity.x += self.walk_acceleration
                self.annimation = self.walk_animation
                self.sprite_flipped = False
        if keys[pygame.K_a] :
            if self.velocity.x > (-self.max_walk_speed) :
                self.velocity.x -= self.walk_acceleration
                self.annimation = self.walk_animation
                self.sprite_flipped = True
        if keys[pygame.K_w] :
            if self.is_grounded == True :
                self.is_grounded = False
                self.velocity.y -= self.jump_velocity
        
        if abs(self.velocity.x) <= self.walk_animation_threashold :
            self.annimation = None


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
        if self.annimation == None :
            self.image = self.frames[0]
        else :
            if self.sprite_flipped :
                self.image = pygame.transform.flip(self.frames[self.annimation.animate()], True, False).convert_alpha()
                self.image.set_colorkey((0, 0, 0))
            else :
                self.image = self.frames[self.annimation.animate()]

        # Update Player
        self.rect.x += self.velocity.x * delta_time
        self.rect.y += self.velocity.y * delta_time
       
    # Getters / Setters
    def set_grounded(self, value : bool) :
        self.is_grounded = value
    def get_grounded(self) -> bool :
        return self.is_grounded
