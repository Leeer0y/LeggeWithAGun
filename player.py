import pygame
from pygame.sprite import Sprite
import entity
import spritesheet
from zombie import Zombie
# TODO
# Make direction a vector, and velocity a scalar quantity


class Player(entity.Entity):
    def __init__(self) -> None:
        super().__init__((172, 148))

        # Sprite loading and Animations
        self.frames_idle = spritesheet.SpriteSheet("./Assets/Sprites/Skeloton/Skeleton Idle.png").load_all_images((24, 38))
        self.frames_walk = spritesheet.SpriteSheet("./Assets/Sprites/Skeloton/Skeleton Walk.png").load_all_images((22, 38))
        self.frames_attack = spritesheet.SpriteSheet("./Assets/Sprites/Skeloton/Skeleton Attack.png").load_all_images((43, 38))
        self.frames_die = spritesheet.SpriteSheet("./Assets/Sprites/Skeloton/Skeleton Dead.png").load_all_images((33, 38))

        self.animation_idle = spritesheet.Animation(self.frames_idle, 1500)
        self.animation_walk = spritesheet.Animation(self.frames_walk, 100)
        self.animation_attack = spritesheet.Animation(self.frames_attack, 50)
        self.animation_die = spritesheet.Animation(self.frames_die, 100)

        self.scale_factor = 4
        
        # Calling parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale_by(self.frames_idle[0], self.scale_factor)

        self.animation = self.animation_idle

        # Animation
        self.walk_animation_threashold = 5

        # Flaag
        self.is_attacking = False

        # Game Logic
        self.attack_group = None
        self.health = 100
        self.attack_damage = 60

    def set_animation(self, animation : spritesheet.Animation, flipped = None) :
        if animation == self.animation and self.is_flipped == flipped :
            return
        if self.is_animation_locked :
            return
        if flipped != None :
            self.is_flipped = flipped

        self.animation = animation

    def attack(self) :
        self.set_animation(self.animation_attack.on_end(self, lambda : self.set_is_attacking(False)))
        self.is_animation_locked = True
        self.set_is_attacking(True)
        print(type(self.attack_group))
        if type(self.attack_group) == list :
            hit_range = pygame.Rect(self.rect.x, self.rect.y, 500, 200)
            hit = hit_range.collideobjects(self.attack_group, key=lambda o : o.rect)
            if type(hit) == Zombie :
                    hit.hurt(self.attack_damage)

    def hurt(self, val) :
        self.health -= val
        if self.health <= 0 :
            self.die()

    def die(self) :
        # End of game
        self.set_is_attacking(False)
        self.set_animation(self.animation_die.on_end(self, self.kill()))
        self.is_animation_locked = True
        

    def update(self) :
        super().update()
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
        if keys[pygame.K_e] :
            if self.is_attacking == False :
                self.attack()
        # Animations
        if abs(self.velocity.x) <= self.walk_animation_threashold :
            self.set_animation(self.animation_idle, None)

        if self.animation == None :
            self.image = pygame.transform.scale_by(self.animation_idle.animate(delta_time * 1000), self.scale_factor).convert_alpha()
        else :
            self.image = pygame.transform.scale_by(self.animation.animate(delta_time * 1000), self.scale_factor).convert_alpha()

        if self.is_flipped :
            self.image = pygame.transform.flip(self.image, True, False)

        # Update Player
        self.rect.x += self.velocity.x * delta_time
        self.rect.y += self.velocity.y * delta_time

    # getters/setters
    def set_is_attacking(self, val) :
        self.is_animation_locked = val
        self.is_attacking = val

    def set_attack_list(self, objs) :
        self.attack_group = objs
       


