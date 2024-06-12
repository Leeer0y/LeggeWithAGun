import pygame
import scene
import ui

class MainMenu(scene.Scene) :
    def __init__(self, screen : pygame.Surface, gamestatemgr) -> None :
        super().__init__(screen, gamestatemgr)
        self.ui_obj = ui.UI(screen)
        text1 = ui.Text("Meow", pygame.Vector2(200, 200), pygame.font.SysFont("Consolas", 35))
        text1.render()
        self.ui_obj.add_element(text1)

    def update(self) :
        self.screen.fill((255, 255, 255))
        self.ui_obj.render_all()
