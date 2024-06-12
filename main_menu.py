import pygame
import scene
import ui

class MainMenu(scene.Scene) :
    def __init__(self, screen : pygame.Surface, gamestatemgr) -> None :
        super().__init__(screen, gamestatemgr)
        self.ui_obj = ui.UI(screen)
        text1 = ui.Text().set_colour((255, 0, 0)).set_text("meow").set_position(pygame.Vector2(200, 200))
        button1 = ui.Button().set_text(ui.Text().set_text("Freaky").set_colour((255, 255, 255)))
        self.ui_obj.add_element(button1)
        self.ui_obj.add_element(text1)

    def update(self) :
        self.screen.fill((255, 255, 255))
        self.ui_obj.render_all()
