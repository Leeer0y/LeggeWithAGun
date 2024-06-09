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
