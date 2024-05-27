import pygame

# TODO
# Make direction a vector, and velocity a scalar quantity

class Player:
    def __init__(self) -> None:
        self.position = pygame.Vector2(0.0, 0.0);
        self.hitbox = pygame.Rect(self.position.x, self.position.y, 20, 20)
       
        # Movement
        self.max_walk_speed = 20

        # Physics
        self.isGrounded = False
        self.mass = 10
        self.coefficent_friction = 0.4 # dertirmened by ground walking on
        self.gravity = 0.9
        self.acceleration = pygame.Vector2(0.0, 0.0)
        self.velocity = pygame.Vector2(0.0, 0.0)
        self.friction = pygame.Vector2(0.0, 0.0)

    def render(self, screen, delta_time) :
        pygame.draw.circle(screen, (255, 255, 255), self.position, 15)
        
        # Update hitbox
        self.hitbox.x = int(self.position.x)
        self.hitbox.y = int(self.position.y)

        # Gravity
        if self.isGrounded == False :
            self.acceleration.y = self.gravity
        else :
            self.acceleration.y = 0.0
            self.velocity.y = 0.0
        
        #Movement
        self.velocity = self.velocity + self.acceleration*delta_time

        if self.velocity != 0 :
            self.position.x += self.velocity.x - (self.mass * self.coefficent_friction) # replace mass with normal force later
        else :
            self.position.x += self.veloctiy.x

        self.position.y += self.velocity.y

