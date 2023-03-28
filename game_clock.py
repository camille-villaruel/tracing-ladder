import pygame

class Clock:
    
    def __init__(self, fps):
        self.fps = fps
        self.clock = pygame.time.Clock()
        
    def set_fps(self):
        self.clock.tick(self.fps)
    
if __name__ == '__main__':
    game_clock = Clock(60)
    print(game_clock.fps)