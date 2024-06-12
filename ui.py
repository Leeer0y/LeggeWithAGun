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

# Determines the positional anchor when setting the postiion of something
class Anchor(enum.Enum) :
    TOP_LEFT = 0
    CENTER = 1

# UI object which takes track of elements in a menu
class UI:
    def __init__(self, screen : pygame.Surface) :
        self.screen = screen
        self.elements : list[Element] = []

    def add_element(self, element) :
        self.elements.append(element)

    def render_all(self) :
        for i in self.elements :
            i.render(self.screen)

# Element base class, Note Elements use method cascading
class Element :
    def __init__(self) -> None:
        # Variables
        self.position : pygame.Vector2 = pygame.Vector2(0, 0)
        self.size : tuple = (0, 0)
        self.anchor = Anchor.TOP_LEFT

    def render(self, screen : pygame.Surface) :
        print("meow")

    def set_position(self, vec2 : pygame.Vector2) :
        self.position = vec2
        self.apply_anchor()
        return self

    def get_position(self) -> pygame.Vector2 :
        return self.position

    def set_anchor(self, anchor : Anchor) :
        self.anchor = anchor
        self.apply_anchor()
        return self

    def apply_anchor(self) :
        pos = self.position
        if self.anchor == Anchor.CENTER :
            pos = pygame.Vector2(self.position.x - self.size[0] / 2,
                                 self.position.y - self.size[1] / 2)

        self.position = pos 

# Text element 
class Text(Element) :
    def __init__(self) -> None:
        super().__init__() 
        self.text : str = "text"
        self.font : pygame.font.Font = pygame.font.SysFont("Consolas", 24)
        self.size = self.font.size(self.text) # set the base size variable so anchoring works
        self.colour : tuple = (0, 0, 0)

    # Getters / Setters
    def set_text(self, text) :
        self.text = text
        self.text_change_event()
        return self

    def set_font(self, font) :
        self.font = font
        self.text_change_event()
        return self

    def set_colour(self, colour) :
        self.colour = colour
        return self

    # happens whenever the texts position or size changes
    def text_change_event(self) :
        self.size = self.font.size(self.text)
        #self.apply_anchor()

    def render(self, screen : pygame.Surface) :
        rendered = self.font.render(self.text, True, self.colour) # Returns a surface object
        screen.blit(rendered, self.position)

class Button(Element) : 
    def __init__(self) -> None:
        super().__init__()
        self.text_obj : Text = Text()
        self.size = (200, 100)
        
        self.button_colour : tuple = (25, 25, 25)
        self.highlight_colour : tuple = (200, 200, 200)
        self.current_colour = self.button_colour

        self.button_rect = pygame.Rect(self.position.x, self.position.y, self.size[0], self.size[1])

        self.text_obj.set_anchor(Anchor.CENTER)

        self.button_event : function = lambda : print("Pressed")

    # a function which updates the buttons rect to ensure it actually moves
    def update_rect(self) :
        self.button_rect = pygame.Rect(self.position.x, self.position.y, self.size[0], self.size[1])

    def set_position(self, vec2: pygame.Vector2):
        super().set_position(vec2)
        self.text_obj.set_position(vec2)
        return self

    def apply_anchor(self):
        super().apply_anchor()
        self.update_rect() # Extend apply anchor base function to update the button rect

    # Getters/setters
    def get_text_obj(self) -> Text :
        return self.text_obj
    def set_text_obj(self, obj, anchor = Anchor.CENTER) :
        self.text_obj = obj
        self.text_obj.set_anchor(anchor)
        self.text_obj.set_position(pygame.Vector2(self.button_rect.center))
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

    # Sets the function to occour when the button is pressed
    def set_event(self, func) :
        self.button_event = func
        return self

    # Represents when a button is hovered
    def highlight(self) :
        self.current_colour = self.highlight_colour
        if pygame.mouse.get_pressed()[0]:
            self.button_event()

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


    
