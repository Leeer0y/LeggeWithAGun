####################
# Title: UI module - Revision
# Author: Leo Pearce
# Date: 6 Dec 2023 
# Revised: 12 Jun 2024
# Description: Handles all ui of the game and displaying menus
####################

from typing import override
import pygame
import json

class UI:
    def __init__(self, screen : pygame.Surface) :
        self.screen = screen
        self.elements = []

    def add_element(self, element) :
        self.elements.append(element)

    def render_all(self) :
        for i in self.elements :
            self.screen.blit(i.rendered, i.position)

class Element :
    def __init__(self, position : pygame.Vector2) -> None:
        self.position = position

    def render(self) :
        print("hello")

class Text (Element):
    def __init__(self, text, position, font : pygame.font.Font) -> None:
        super().__init__(position) 
        self.text = text
        self.font = font
        self.colour = (0, 0, 0)
        self.rendered = None

    def set_position(self, vec2 : pygame.Vector2) :
        self.position = vec2
        return self
    
    def set_text(self, text) :
        self.text = text
        return self

    def render(self) :
        self.rendered = self.font.render(self.text, True, self.colour)
    
