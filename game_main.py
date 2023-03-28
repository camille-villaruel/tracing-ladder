import pygame
from game_start import Start
from game_board import Board
from game_clock import Clock
from game_ladder import Ladder

game_start = Start(running=True)
init_game = game_start.start

game_clock = Clock(fps=60)
init_clock = game_clock.clock

game_board = Board(
        size = (1280, 720),
        game_bg = 'bg/wallpaper.jpg',
        game_font = 'font/game_plan/GamePlan - Dker.ttf',
        game_font_size = 50
        )

game_ladder = Ladder(
    game_board.bg_surface
)

game_caption = Board.set_game_caption('Load the File')

text_font = game_board.set_game_font()
text_surface = Board.render_text(text_font, 'Hello', 'Blue', True)

rect_dimensions = (40, game_board.screen.get_width())

game_ladder.set_margin_attributes()
game_ladder.create_grid()
game_ladder.generate_steps_pos(3)
game_ladder.generate_steps_dims()
print(game_ladder.steps_dict)
print(game_ladder.steps_dim_dict)

game_ladder.create_steps()
print(game_ladder.steps_rect_dict)

while game_start.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start.end_game()
    
    game_board.screen.blit(game_board.bg_surface, (0,0))
   
    
    # game_board.screen.blit(text_surface, (0,0))
    pygame.display.flip()
    game_clock.set_fps()
