import pygame
import scene
import ui

class MainMenu(scene.Scene) :
    def __init__(self, screen : pygame.Surface, gamestatemgr) -> None :
        super().__init__(screen, gamestatemgr)

        # UI objects
        self.ui_obj = ui.UI(screen)
        play_text = ui.Text().set_text("Play").set_colour((255, 255, 255))
        button_play = ui.Button().set_position(pygame.Vector2(screen.get_rect().center)).set_anchor(ui.Anchor.CENTER).set_text_obj(play_text)
        button_play = button_play.set_event(lambda : self.game_state_manager.set_state('infinite'))
        
        self.ui_obj.add_element(button_play)

    def update(self) :
        self.screen.fill((255, 255, 255))
        self.ui_obj.render_all()
