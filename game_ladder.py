import pygame
import json
from util import generate_steps_by_number

default_col_number = 4

def get_screen_margin_dict():
    with open('screen_margin.json', 'r') as f:
        screen_file = f.read()

    return json.loads(screen_file)
    
screen_margin  = get_screen_margin_dict()

class Ladder:
    
    def __init__(self, screen_surface):
        self.screen_surface = screen_surface
        self.screen_width = self.screen_surface.get_width()
        self.screen_height = self.screen_surface.get_height()
        self.ladder_width = screen_margin['ladder_width']

    def set_margin_attributes(self):
        self.center_width = self.screen_width / 2 - 1
        self.center_height = self.screen_height / 2 
        self.top_margin = screen_margin['top_width_margin']
        self.left_margin = screen_margin['left_width_margin']
        self.right_margin = screen_margin['right_width_margin']
        self.bottom_margin = screen_margin['bottom_width_margin']
        self.top_sec_margin = screen_margin['top_secondary_width']
    
    def create_grid(self):

        self.top_rect = pygame.draw.line(self.screen_surface, screen_margin['top_color'], (self.center_width, 0), 
                                         (self.center_width, self.top_margin), self.screen_width)
        
        self.bottom_rect = pygame.draw.line(self.screen_surface, screen_margin['bottom_color'], (self.center_width, self.screen_height - self.bottom_margin), 
                                            (self.center_width, self.screen_height), self.screen_width)
        
        self.top_margin_rect = pygame.draw.line(self.screen_surface, screen_margin['top_margin_color'], (self.center_width, self.top_rect.bottom),
                                                (self.center_width, self.top_rect.bottom + self.top_sec_margin), self.screen_width)
        
        self.left_rect = pygame.draw.line(self.screen_surface, screen_margin['left_right_color'], (self.left_margin/2, self.top_margin_rect.bottom),
                                          (self.left_margin/2, self.bottom_rect.top), self.left_margin)
        
        self.right_rect = pygame.draw.line(self.screen_surface, screen_margin['left_right_color'], (self.screen_width - self.right_margin/2, self.top_margin_rect.bottom),
                                          (self.screen_width - self.right_margin/2, self.bottom_rect.top), self.right_margin)
        
        self.left1_rect = pygame.draw.line(self.screen_surface, screen_margin['ladder_color'], (self.left_rect.right + self.ladder_width /2, self.top_margin_rect.bottom),
                                           (self.left_rect.right + self.ladder_width /2, self.bottom_rect.top), self.ladder_width)
        
        self.right1_rect = pygame.draw.line(self.screen_surface, screen_margin['ladder_color'], (self.right_rect.left - self.ladder_width /2, self.top_margin_rect.bottom),
                                           (self.right_rect.left - self.ladder_width /2, self.bottom_rect.top), self.ladder_width)
        
        self.center_col_rect = pygame.draw.line(self.screen_surface, screen_margin['ladder_color'], (self.center_width, self.top_margin_rect.bottom),
                                                 (self.center_width, self.bottom_rect.top), self.ladder_width)
        
        left2_screen_start_pos = self.left1_rect.right + (self.center_col_rect.left - self.left1_rect.right)/ 2 - self.ladder_width/2
        
        self.left2_rect = pygame.draw.line(self.screen_surface, screen_margin['ladder_color'], (left2_screen_start_pos, self.top_margin_rect.bottom),
                                           (left2_screen_start_pos, self.bottom_rect.top), self.ladder_width)
        
        right2_screen_start_pos = self.right1_rect.left - (self.center_col_rect.left - self.left1_rect.right)/ 2 - self.ladder_width/2
        
        self.right2_rect = pygame.draw.line(self.screen_surface, screen_margin['ladder_color'], (right2_screen_start_pos, self.top_margin_rect.bottom),
                                           (right2_screen_start_pos, self.bottom_rect.top), self.ladder_width)
    
    def generate_steps_pos(self, steps_number):
        self.steps_dict = dict()
        
        start_rand = self.top_margin_rect.bottom + self.ladder_width
        end_rand = self.bottom_rect.top - self.ladder_width
        
        for i in range(0, default_col_number):
            self.steps_dict[i] = generate_steps_by_number(steps_number, start_rand, end_rand)
        
    def generate_steps_dims(self):
        self.steps_dim_dict = dict()
        
        left_step_dims = [self.left1_rect.right, self.left2_rect.right, self.center_col_rect.right, self.right2_rect.right]
        right_step_dims = [self.left2_rect.left, self.center_col_rect.left, self.right2_rect.left, self.right1_rect.left]
        
        for i in range(0, default_col_number):
           self.steps_dim_dict[i] = (left_step_dims[i], right_step_dims[i])
        
    def create_steps(self):
        self.steps_rect_dict = dict()
        
        for col_number, step_values in self.steps_dict.items():
            steps_rect_dict_sub = dict()
            for step_number, step_pos_value in step_values.items():
                step_height = step_pos_value
                
                left_step_lim = self.steps_dim_dict[col_number][0]
                right_step_lim = self.steps_dim_dict[col_number][1]
                
                step_width = abs(left_step_lim - right_step_lim)
                step_hor_dim = left_step_lim + int(step_width/2 - 1 )
                
                steps_rect_dict_sub[step_number] = pygame.draw.line(self.screen_surface, screen_margin['ladder_color'], (step_hor_dim, step_height),
                                                                     (step_hor_dim, step_height + self.ladder_width), step_width)
            self.steps_rect_dict[col_number] = steps_rect_dict_sub
            
            