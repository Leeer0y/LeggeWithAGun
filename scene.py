#############################
# Author: Leo Pearce
# Created: 10/6/24
# Last Edited: 13/6/24
# Description: The scence class, contains nececary componetnts for a scene object and allows type checking and
# error provention
#############################

import pygame

class Scene :
    def __init__(self, screen : pygame.Surface, gamestatemngr) :
        self.screen = screen
        self.game_state_manager =  gamestatemngr
        self.background_colour = ((255, 255, 255))
        
    def change(self, scene) :
        return scene

    def update(self) :
        self.screen.fill(self.background_colour)
