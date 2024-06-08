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



class animation:
    def __init__(self, frames : list[int], time : float) -> None:
        self.frame_sequence = frames # frame numbers in order of animation
        self.animation_time = time # (seconds) time that it takes for the animation to finish
        
        self.current_itteration = 0
        self.clock = pygame.time.Clock()

        self.animation_percentage = 0.0 # percentage of progress through the animation
        self.animation_step = 1 + len(self.frame_sequence) / self.animation_time # percentage to get to the next frame
        self.animation_time_passed = 0.0

    def timer(self) :
        # think of the ammount of frames in the animation like fps
        self.clock.tick()
        delta_time = self.clock.get_time() # Time between calls (secconds)
        self.animation_time_passed += delta_time
        self.animation_percentage = self.animation_time_passed/self.animation_time # results in total time passed / goal time - percetnatge of completation

        if (self.animation_percentage >= self.animation_step*(self.current_itteration + 1)) :
            return True
        
        return False
    
    def animate(self):
        if self.timer():
            # Timer has ticked, its time to change to the next frame in the animation
            if (self.current_itteration < len(self.frame_sequence) - 1):
                self.current_itteration += 1
            else :
                self.current_itteration = 0
                self.animation_percentage = 0
                self.animation_time_passed = 0

        return self.frame_sequence[self.current_itteration]

