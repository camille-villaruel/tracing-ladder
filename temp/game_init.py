# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

title_font = pygame.font.Font('font/game_plan/GamePlan - Dker.ttf', 50)

bg_surface = pygame.image.load('bg/wallpaper.jpg').convert()

text_surface = title_font.render('Tracing Ladder Game', True, 'White')

player_surface = pygame.image.load('player/car-64.png').convert_alpha()

player_x, player_y = screen.get_width() / 2, screen.get_height() / 2

player_rect = player_surface.get_rect(midbottom = (player_x, player_y))


dt = 3
pos = 0
#rectA.colliderect(rectB) bool output - if rect A hits rect B
#rectA.collidepoint((x,y)) + using the mouse

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         print('right')
        #     if event.key == pygame.K_LEFT:
        #         print('left')
    # fill the screen with a color to wipe away anything from last frame   
    screen.blit(bg_surface, (0,0))
    screen.blit(text_surface, (screen.get_width() / 2 - (text_surface.get_width() / 2), 10))
    
    # RENDER YOUR GAME HERE
    # pygame.draw.circle(screen, "orange", player_pos, 40)
    
    
    line_rect = pygame.draw.line(screen, '#2F2828' , (screen.get_width() / 2,  screen.get_height() / 2), (screen.get_width() / 2, screen.get_height() / 2 + 100), 25)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        # player_pos.y -= 300 * dt
        print('w')
        pos -= 10
        if player_y >= screen.get_height():
            player_y = screen.get_height() - player_surface.get_height()
            
        player_rect = player_rect.move(0, pos)
        print('pos:', pos)
        print('player_rect:', player_rect)
    
    if keys[pygame.K_s]:
        # player_pos.y += 300 * dt
        print('s')

    if keys[pygame.K_a]:
        # player_pos.x -= 300 * dt
        print('a')

    if keys[pygame.K_d]:
        # player_pos.x += 300 * dt
        print('d')

    screen.blit(player_surface, player_rect)
    # flip() the display to put your work on screen
      
    
    clock.tick(60) # limits FPS to 60

pygame.quit()