import pygame

class sheet:
    def __init__(self, image_path):
        self.sheet = pygame.image.load(image_path)
        if not self.sheet :
            print("Sprite sheet with path" + image_path + " not loaded")
        
        self.current_frame = 0 # frame number (int)
        self.frames = [] # List of frames
        self.animations = {} # animation dictionary

    def load_frames(self, frame_size):
       # Get number of frames from image frame_size
        frame_spec = (int(self.sheet.get_width() / frame_size[0]), int(self.sheet.get_height() / frame_size[1])) # How many rows and columns, (#frame in coloum, #frame in row)
        width = frame_size[0]
        height = frame_size[1]

        for y in range(frame_spec[1]):
            # For every row
            for x in range(frame_spec[0]):
                # for every column
                frame = pygame.Surface((width,  height)).convert_alpha()
                frame.blit(self.sheet, (0, 0), ((width * x), (height * y), width, height))
                frame.set_colorkey((0, 0, 0))
                self.frames.append(frame)

        self.current_frame = self.frames[0]

    def add_animation(self, name, animation) :
        self.animations[name] = animation
        return

    def animate(self, animation_name):
        if self.animations[animation_name] :
            self.current_frame = self.animations[animation_name].animate()



class animation:
    def __init__(self, frames : list[int], time : float) -> None:
        self.frame_sequence = frames # List of frame numbers in order of animation
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

