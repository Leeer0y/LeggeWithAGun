#############################
# Author: Leo Pearce
# Created: 10/6/24
# Last Edited: 13/6/24
# Description: The games main infinite gamemode scene
#############################

import pygame
import scene
import player
import zombie
import gemoetry
import random
import ui

class Infinite(scene.Scene) :
    def __init__(self, screen: pygame.Surface, gamestatemgr) -> None:
        super().__init__(screen, gamestatemgr)

        self.player = player.Player()
        self.player.rect.x = 400
        
        self.zombie = zombie.Zombie()
        self.zombie.rect.x = 600

        self.ground = gemoetry.rect((0, 0, 0), pygame.Rect(0, 790, 800, 20))

        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        self.entities.add(self.zombie)

        self.monsters = [self.zombie]

        self.geometry = pygame.sprite.Group()
        self.geometry.add(self.ground)

        self.sidescroll_group = pygame.sprite.Group()
        self.sidescroll_group.add(self.player)

        self.clock = pygame.time.Clock()

        self.sidescroll_speed = 35
        self.zombie_chance = 20 # percent
        self.zombie_timer = 0.0
        self.zombie_timer_trigger = 1.0
        self.zombie_chance_multiplier = 2.5

        self.level = 0 
        self.level_timer = 0.0
        self.next_level_time = 10.0
        self.level_special = 5
        self.level_time_addition = 4

        self.player.set_attack_list(self.monsters)
        self.zombie.set_target(self.player)

        # UI stuffs
        self.ui_background = ui.UI(self.screen)
        self.ui_foreground = ui.UI(self.screen)

        self.level_text = ui.Text().set_text("Level: 0").set_font(pygame.font.Font("./Assets/Fonts/RubikPixels-Regular.ttf", 50)).set_colour((50, 50, 50))
        self.level_text = self.level_text.set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen.get_rect().center[0], 100))
        self.ui_background.add_element(self.level_text)

        self.health_text = ui.Text().set_text(str(self.player.health)).set_font(pygame.font.Font("./Assets/Fonts/Tiny5-Regular.ttf", 30)).set_colour((255, 0, 0))
        self.ui_foreground.add_element(self.health_text)
        
        # Difficulty Selection
        screen_center = pygame.Vector2(screen.get_rect().center)
        self.has_chosen_difficulty = False
        self.can_choose = False
        self.ui_difficulty = ui.UI(screen)
        button_easy_text  = ui.Text().set_text("Easy").set_colour((255, 255, 255))
        button_easy = ui.Button().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y - 150)).set_text_obj(button_easy_text)
        button_easy = button_easy.set_event(lambda : self.set_difficulty(0))

        button_med_text  = ui.Text().set_text("Medium").set_colour((255, 255, 255))
        button_med = ui.Button().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y)).set_text_obj(button_med_text)
        button_med = button_med.set_event(lambda : self.set_difficulty(1))
        
        button_hard_text  = ui.Text().set_text("Hard").set_colour((255, 255, 255))
        button_hard = ui.Button().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y + 150)).set_text_obj(button_hard_text)
        button_hard = button_hard.set_event(lambda : self.set_difficulty(2))
        
        self.ui_difficulty.add_element(button_easy)
        self.ui_difficulty.add_element(button_med)
        self.ui_difficulty.add_element(button_hard)
    
    def update(self) :
        self.screen.fill((19, 26, 48))
        
        if self.can_choose == False :
            if pygame.mouse.get_pressed()[0] != True :
                self.can_choose = True
        if self.has_chosen_difficulty == True :
            self.game_loop()
        else :
            if self.can_choose == True :
                self.ui_difficulty.render_all()

    def game_loop(self):
        # Timing
        delta_time = self.clock.get_time() / 1000

        # Background UI
        self.ui_background.render_all()

        # Random platform generation
        self.zombie_timer += delta_time
        if self.zombie_timer >= self.zombie_timer_trigger :
            self.generate_zombie()
            self.zombie_timer = 0.0
        
        # Level timer 
        self.level_timer += delta_time
        if self.level_timer >= self.next_level_time :
           self.next_level() 

        # Drawing Sprites

        self.entities.draw(self.screen)
        self.entities.update()
        #self.zombie.go_to(pygame.Vector2(self.player.rect.x, self.player.rect.y))
        
        self.geometry.draw(self.screen)

        # Foreground UI
        self.health_text.set_text(str(self.player.health))
        self.ui_foreground.render_all()

        # Colision
        for i in self.entities.sprites() :
            if pygame.sprite.collide_rect(i, self.ground) :
                i.set_grounded(True)
            else :
                i.set_grounded(False)

        self.clock.tick()

    def next_level(self) :
        print("plug")
        self.level += 1
        self.level_text.set_text("Level: " + str(self.level))
        if self.level % self.level_special == 0 :
            # No remainder therefore devisiable by speical level number
            # speical level, replenish health ect 
            self.player.health = 100 
        self.level_timer = 0.0 
        self.next_level_time += self.level_time_addition

        if self.zombie_chance < 100 :
            self.zombie_chance += self.zombie_chance_multiplier

    def generate_zombie(self) :
        if random.randint(0, 100) < self.zombie_chance :
            z = zombie.Zombie()
            z.set_position(pygame.Vector2(random.randint(0, 800), 0))
            z.set_target(self.player)
            z.health = random.randint(70, 120)
            self.entities.add(z)
            self.monsters.append(z)
            self.player.set_attack_list(self.monsters)

    # 0 = Easy | 1 = Medium | 2 = Hard
    def set_difficulty(self, difficulty) :
        if difficulty == 0 :
            self.player.attack_damage = 100
            self.player.health = 1200
        if difficulty == 1 :
            self.player.attack_damage = 75
            self.player.health = 1000
        if difficulty == 2 :
            self.player.attack_damage = 50
            self.player.health = 800

        self.has_chosen_difficulty = True


