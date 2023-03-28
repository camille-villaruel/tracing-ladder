import pygame

class Start:
    
    def __init__(self, running):
        self.running = running
        self.start = pygame.init()
        
    def end_game(self):
        self.running = False
        

if __name__ == '__main__':
    game_start = Start(True)
    game_start.end_game()
    print(game_start.running)
    