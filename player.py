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
        self.walk_speed = 0.0
        self.max_walk_speed = 100.0
        self.walk_acceleration = 26
        
        self.jumpVelocity = 90

        #Physics
        self.velocity = pygame.Vector2(0.0, 0.0)
        self.gravity = 9.8
        self.friction = 3

    def player_controls(self) :
        keys = pygame.key.get_pressed()
        
        # Movement
        if keys[pygame.K_d] :
            if self.velocity.x < self.max_walk_speed :
                self.velocity.x += self.walk_acceleration
        if keys[pygame.K_a] :
            if self.velocity.x > (-self.max_walk_speed) :
                self.velocity.x -= self.walk_acceleration
        if keys[pygame.K_w] :
            self.velocity.y -= self.jumpVelocity
            #print(self.velocity * delta_time)
                
    def render(self, screen, delta_time, collision_list) :
        pygame.draw.circle(screen, (255, 255, 255), self.position, 15)
        
        # Collisions
        collisions = self.hitbox.collidelistall(collision_list)
        if collisions :
            #test ground
            for i in collisions :
                if collision_list[i].top <= self.hitbox.bottom :
                    self.IsGrounded = True
        else :
            self.IsGrounded = False
        

        # Gravity
        if self.IsGrounded == False :
            self.velocity.y += self.gravity
        else :
            if self.velocity.y > 0.0 :
                self.velocity.y = 0.0

            #friction
            if self.velocity :
                direction_travelling = self.velocity.normalize() # The higher the velocity in a direction, the closer it will be to 1
                if abs(self.velocity.magnitude()) > self.friction :
                    print(direction_travelling * self.friction)
                    self.velocity -= (direction_travelling * self.friction)
                else :
                    self.velocity = direction_travelling * 0

        # Movement
        self.player_controls()
        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time

        # Update hitbox
        self.hitbox.x = int(self.position.x)
        self.hitbox.y = int(self.position.y)
