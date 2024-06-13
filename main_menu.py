#############################
# Author: Leo Pearce
# Created: 10/6/24
# Last Edited: 13/6/24
# Description: The main menu scene
#############################

import pygame
import scene
import ui

class MainMenu(scene.Scene) :
    def __init__(self, screen : pygame.Surface, gamestatemgr) -> None :
        super().__init__(screen, gamestatemgr)

        # Quicktype Variables
        screen_center = pygame.Vector2(screen.get_rect().center)

        # UI objects
        self.ui_main = ui.UI(screen)
        self.ui_help = ui.UI(screen)
        
        close_button_text = ui.Text().set_text("Close").set_colour((255, 255, 255))
        button_close = ui.Button().set_position(pygame.Vector2(screen_center)).set_anchor(ui.Anchor.CENTER).set_text_obj(close_button_text)
        button_close.set_event(lambda : self.set_menu(self.ui_main))

        # Help Menu
        help_text_htp_title = ui.Text().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y - 220))
        help_text_htp_title = help_text_htp_title.set_text("How to play").set_colour((255, 255, 255))
        help_text_htp_1 = ui.Text().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y - 200))
        help_text_htp_1 = help_text_htp_1.set_text("Your goal is to try and survive as long as possible.").set_colour((255, 255, 255))
        help_text_htp_2 = ui.Text().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y - 180))
        help_text_htp_2 = help_text_htp_2.set_text("Kill zombies to survive").set_colour((255, 255, 255))

        help_text_ctrl_title = ui.Text().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y + 100))
        help_text_ctrl_title = help_text_ctrl_title.set_text("Controls").set_colour((255, 255, 255))
        help_text_ctrl_1 = ui.Text().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y + 120))
        help_text_ctrl_1 = help_text_ctrl_1.set_text("Movement : A D W(Jump) ").set_colour((255, 255, 255))
        help_text_ctrl_2 = ui.Text().set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, screen_center.y + 140))
        help_text_ctrl_2 = help_text_ctrl_2.set_text("Attack : E ").set_colour((255, 255, 255))

        self.ui_help.add_element(help_text_htp_title)
        self.ui_help.add_element(help_text_htp_1)
        self.ui_help.add_element(help_text_htp_2)
        self.ui_help.add_element(help_text_ctrl_title)
        self.ui_help.add_element(help_text_ctrl_1)
        self.ui_help.add_element(help_text_ctrl_2)
        self.ui_help.add_element(button_close.set_position(pygame.Vector2(screen_center.x, screen_center.y + 300)))
        
        # Main Menu
        title_text = ui.Text().set_text("Skeleton Vs Zombies").set_font(pygame.font.Font("./Assets/Fonts/RubikPixels-Regular.ttf", 50)).set_anchor(ui.Anchor.CENTER).set_position(pygame.Vector2(screen_center.x, 50)).set_colour((255, 40, 40))

        play_text = ui.Text().set_text("Play").set_colour((255, 255, 255))
        button_play = ui.Button().set_position(pygame.Vector2(screen_center)).set_anchor(ui.Anchor.CENTER).set_text_obj(play_text)
        button_play = button_play.set_event(lambda : self.game_state_manager.set_state('infinite'))
       
        button_help_text = ui.Text().set_text("Help").set_colour((255, 255, 255))
        button_help = ui.Button().set_position(pygame.Vector2(screen_center.x, screen_center.y + 150)).set_anchor(ui.Anchor.CENTER).set_text_obj(button_help_text)
        button_help = button_help.set_event(lambda : self.set_menu(self.ui_help))
        self.ui_main.add_element(title_text)
        self.ui_main.add_element(button_play)
        self.ui_main.add_element(button_help)


        self.current_menu = self.ui_main
        self.has_released_mouse = False

    def update(self) :
        self.screen.fill((0, 0, 0))
        if self.has_released_mouse == True :
            self.current_menu.render_all()
        else :
            if pygame.mouse.get_pressed()[0] == False :
                self.has_released_mouse = True

    def set_menu(self, menu) :
        self.current_menu = menu
