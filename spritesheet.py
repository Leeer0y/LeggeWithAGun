from collections.abc import Sequence
import pygame
from pygame.surface import Surface

class SpriteSheet:
    def __init__(self, image_path):
        self.sheet = pygame.image.load(image_path)

    def load_all_images(self, frame_size):
        images = []
        width = frame_size[0]
        height = frame_size[1]
        for row in range(int(self.sheet.get_height() / height)):
            # for every row in the image
            for collumn in range(int(self.sheet.get_width() / width)):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(self.sheet, (0, 0), ((width * collumn), (height * row), width, height))
                image.set_colorkey((0, 0, 0))
                images.append(image)

        return images

    def load_images(self, frame_size, frames) :
        all_images = self.load_all_images(frame_size)
        images = []

        for i in frames:
            images.append(all_images[i])

        return images



class Animation :
    def __init__(self, frames : list[pygame.Surface], time : float, sequence = None) -> None:
        self.frames = frames
        self.animation_time = time
        self.sequence = sequence
        
        self.clock = pygame.time.Clock()
        self.animation_percentage = 0.0
        self.animation_step = 1 + len(self.frames) / self.animation_time
        self.animation_frame = 0
        
        self.is_flipped = False

    def timer(self) -> bool :
        self.clock.tick()
        delta_time = self.clock.get_time()

        self.animation_percentage += delta_time/self.animation_time
        if self.animation_percentage >= self.animation_step*(self.animation_frame + 1) :
            return True

        return False

    def animate(self) -> pygame.Surface :
        if self.sequence == None :
            self.sequence = list(range(len(self.frames)))

        if self.timer() :
            if self.animation_frame < len(self.sequence) - 1 :
                self.animation_frame += 1
            else :
                self.animation_frame = 0
                self.animation_percentage = 0
       
        frame = self.frames[self.sequence[self.animation_frame]]
        if self.is_flipped :
            return pygame.transform.flip(frame, True, False)

        return frame

    def flipped(self, val = True) :
        self.is_flipped = val
