####################
# Title: UI module - Revision
# Author: Leo Pearce
# Date: 6 Dec 2023 
# Revised: 12 Jun 2024
# Description: Handles all ui of the game and displaying menus
####################

from typing import override
import pygame
import enum
import json

class Anchor(enum.Enum) :
    TOP_LEFT = 0
    CENTER = 1

class UI:
    def __init__(self, screen : pygame.Surface) :
        self.screen = screen
        self.elements : list[Element] = []

    def add_element(self, element) :
        self.elements.append(element)

    def render_all(self) :
        for i in self.elements :
            i.render(self.screen)

class Element :
    def __init__(self) -> None:
        self.position : pygame.Vector2 = pygame.Vector2(0, 0)

    def render(self, screen : pygame.Surface) :
        print("meow")

    def get_position(self) -> pygame.Vector2 :
        return self.position

class Text(Element) :
    def __init__(self) -> None:
        super().__init__() 
        self.text : str = "text"
        self.font : pygame.font.Font = pygame.font.SysFont("Consolas", 24)
        self.colour : tuple = (0, 0, 0)

        self.position_anchor : Anchor = Anchor.TOP_LEFT

    def set_position(self, vec2 : pygame.Vector2) :
        self.position = vec2
        self.apply_anchor()
        return self
    
    def set_text(self, text) :
        self.text = text
        self.apply_anchor()
        return self

    def set_font(self, font) :
        self.font = font
        self.apply_anchor()
        return self

    def set_colour(self, colour) :
        self.colour = colour
        return self

    def set_anchor(self, anchor : Anchor) :
        self.position_anchor = anchor
        self.apply_anchor()
        return self

    def apply_anchor(self) :
        pos = self.position
        font_size = self.font.size(self.text)
        if self.position_anchor == Anchor.CENTER :
            pos = pygame.Vector2(self.position.x - font_size[0] / 2,
                                 self.position.y - font_size[1] / 2)

        self.position = pos

    def render(self, screen : pygame.Surface) :
        rendered = self.font.render(self.text, True, self.colour)
        screen.blit(rendered, self.position)

class Button(Element) : 
    def __init__(self) -> None:
        super().__init__()
        self.text_obj : Text = Text()
        self.size : tuple = (200, 100)
        
        self.button_colour : tuple = (25, 25, 25)
        self.highlight_colour : tuple = (200, 200, 200)
        self.current_colour = self.button_colour

        self.button_rect = pygame.Rect(self.position.x, self.position.y, self.size[0], self.size[1])

        self.text_obj.set_anchor(Anchor.CENTER)

    def get_text(self) -> Text :
        return self.text_obj
    def set_text(self, obj, anchor = Anchor.CENTER) :
        self.text_obj = obj
        self.text_obj.set_position(pygame.Vector2(self.button_rect.center))
        self.text_obj.set_anchor(anchor)
        return self

    def set_size(self, size) :
        self.size = size
        return self

    def set_button_colour(self, colour) :
        self.button_colour = colour
        return self

    def set_hightlight_colour(self, colour) :
        self.highlight_colour = colour
        return self

    def highlight(self) :
        self.current_colour = self.highlight_colour
    def un_highlight(self) :
        self.current_colour = self.button_colour

    def render(self, screen : pygame.Surface) :
        pygame.draw.rect(screen, self.current_colour, self.button_rect)
        self.text_obj.render(screen)

        # Mouse stuffs
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos) :
            self.highlight()
        else :
            self.un_highlight()


    
