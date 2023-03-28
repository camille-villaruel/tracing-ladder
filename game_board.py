import pygame

class Board:
    def __init__(self, size, game_bg, game_font, game_font_size):
        self.size = size
        self.game_bg = game_bg
        self.game_font = game_font
        self.game_font_size = game_font_size
        
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font(self.game_font, self.game_font_size)
        self.bg_surface = pygame.image.load(self.game_bg).convert()
    
    def set_display(self):
        self.screen = pygame.display.set_mode(self.size)
    
    def set_design_bg(self):
        self.bg_surface = pygame.image.load(self.game_bg).convert()
        return self.bg_surface
    
    def set_game_font(self):
        self.font = pygame.font.Font(self.game_font, self.game_font_size)
        return self.font
    
    @staticmethod
    def set_game_caption(string_text):
        pygame.display.set_caption(string_text)
    
    @staticmethod
    def render_text(text_font, string_text, string_color, aliasing):
        text_surface = text_font.render(string_text, aliasing, string_color)
        return text_surface

if __name__ == '__main__':
    pygame.init()