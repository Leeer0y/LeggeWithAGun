from collections.abc import Sequence
import pygame
import ctypes
from pygame.surface import Surface

class SpriteSheet:
    def __init__(self, image_path):
        self.sheet = pygame.image.load(image_path)

    # load all sprites
    def load_all_images(self, frame_size):
        images = []
        width = frame_size[0] # size of sprite in sheet
        height = frame_size[1] # size of sprite in sheet

        for row in range(int(self.sheet.get_height() / height)):
            # for every row in the image
            for collumn in range(int(self.sheet.get_width() / width)):
                # for evey colum in the image
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(self.sheet, (0, 0), ((width * collumn), (height * row), width, height))
                image.set_colorkey((0, 0, 0))
                images.append(image)

        return images

    # load a row of a sprite sheet (frames = how many frames you want to get)
    def load_row(self, frame_size, row, frames = None) -> list[pygame.Surface] :
        images = []
        width = frame_size[0]
        height = frame_size[1]

        # for every sprite in the row
        for i in range(int(self.sheet.get_width() / width)) :
            if frames :
                if i + 1 > frames : break
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(self.sheet, (0, 0), ((width * i), (height * row), width, height))
            image.set_colorkey((0, 0, 0))
            images.append(image)

        return images

    # load specified frames
    def load_images(self, frame_size, frames) :
        all_images = self.load_all_images(frame_size)
        images = []

        for i in frames:
            images.append(all_images[i])

        return images



class Animation :
    def __init__(self, frames : list[pygame.Surface], time : float, sequence = None) -> None:
        self.frames = frames # list of sprite images
        self.animation_time = time # the desired time for the animatmion to complete one cycle
        self.sequence = sequence # the order of the animation (frame indexes, ints)
        
        self.clock = pygame.time.Clock() 
        self.animation_percentage = 0.0
        self.animation_step = 1 + len(self.frames) / self.animation_time # the required percentage for the animation to change
        self.animation_frame = 0 # current frame index, used for calulations
        
        self.is_flipped = False # Flip flag

        # Hooks
        self.end_hook = None
        self.end_hook_obj = None

    def timer(self) -> bool :
        # Update clock
        delta_time = self.clock.get_time()

        self.animation_percentage += delta_time/self.animation_time #  adds the time passed as a percentage of the goal time
        if self.animation_percentage >= self.animation_step*(self.animation_frame + 1) :
            return True

        self.clock.tick()
        return False

    def animate(self) -> pygame.Surface :
        if self.sequence == None :
            # no sequence specified, assume in order
            self.sequence = list(range(len(self.frames)))

        if self.timer() :
            # Every time the sprite is meant to change

            # repeate if index goes out of bounds
            if self.animation_frame < len(self.sequence) - 1 :
                self.animation_frame += 1
            else :
                if self.end_hook != None :
                    self.end_hook()

                self.animation_frame = 0
                self.animation_percentage = 0
       
        frame = self.frames[self.sequence[self.animation_frame]] # the frame to be returned

        # check if the image is flipped
        if self.is_flipped :
            frame = pygame.transform.flip(frame, True, False)

        return frame

    def flipped(self, val = True) :
        self.is_flipped = val
        return self

    # Hooks
    def on_end(self, obj, func) :
        self.end_hook = func
        self.end_hook_obj = obj
        return self
