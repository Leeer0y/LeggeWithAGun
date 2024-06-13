#############################
# Author(s): Leo Pearce, Coding with Sphere
# Created: 10/6/24
# Last Edited: 10/6/24
# Description: The programs main entry point
# Game state system based of tutorial code : https://youtu.be/r0ixaTQxsUI?si=j-2fb3vEOj-Y9zyM
#############################

import pygame
import sys
import scene

# Scenes
import infinite
import main_menu

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FPS = 60

# Contains basics for the game to run
class Game:
    def __init__(self) -> None:
        pygame.init()
        # Pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # State manager and Scenes
        self.game_state_manager = GameStateManager('main_menu')
        self.main_menu = main_menu.MainMenu(self.screen, self.game_state_manager)
        self.infinite = infinite.Infinite(self.screen, self.game_state_manager) 

        self.states = {'main_menu':self.main_menu, 'infinite':self.infinite}
        self.game_state_manager.on_state_change(lambda : self.reset_state())

    def  run(self):
        # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.states[self.game_state_manager.get_state()].update() # Looks up the state name, gets the scene, then calls the update method

            pygame.display.update()
            self.clock.tick(FPS)

    def reset_state(self) :
        self.states[self.game_state_manager.get_state()].__init__(self.screen, self.game_state_manager)

# Game state manager, basicly a string that any scene can access (a game_state_manager is a required parameter for scenes) and set to change the scene
class GameStateManager:
    def __init__(self, currentState) -> None:
        self.currentState = currentState
        self.state_change_hook : function = lambda : print("state change")
    
    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state
        self.state_change_hook()

    def on_state_change(self, func) :
        self.state_change_hook = func


if __name__ == '__main__':
    game = Game()
    game.run()
