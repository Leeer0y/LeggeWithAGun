import pygame

# TODO
# Make direction a vector, and velocity a scalar quantity

class Player:
    def __init__(self) -> None:
        self.position = pygame.Vector2(0.0, 0.0);
        self.hitbox = pygame.Rect(self.position.x, self.position.y, 20, 20)
      
        # Flags
        self.IsGrounded = False

        # Movement
        self.walk_speed = 0
        self.max_walk_speed = 10
        self.walk_acceleration = 0.2

        #Physics
        self.velocity = pygame.Vector2(0.0, 0.0)
        self.gravity = 0.4

    def player_controls(self, event, delta_time) :
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d :
                self.velocity.x = 20

    def render(self, screen, delta_time) :
        pygame.draw.circle(screen, (255, 255, 255), self.position, 15)
        
        # Update hitbox
        self.hitbox.x = int(self.position.x)
        self.hitbox.y = int(self.position.y)

        # Movement
        

        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time
