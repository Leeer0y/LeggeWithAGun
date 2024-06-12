import pygame
import sys
import scene

# Scenes
import infinite
import main_menu

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FPS = 60

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager('main_menu')
        self.main_menu = main_menu.MainMenu(self.screen, self.game_state_manager)
        self.infinite = infinite.Infinite(self.screen, self.game_state_manager) 

        self.states = {'main_menu':self.main_menu, 'infinite':self.infinite}

    def  run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.states[self.game_state_manager.get_state()].update()

            pygame.display.update()
            self.clock.tick(FPS)

class GameStateManager:
    def __init__(self, currentState) -> None:
        self.currentState = currentState
    
    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()
