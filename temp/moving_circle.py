# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Tracing Ladder Game')
clock = pygame.time.Clock()
running = True
dt = 0

test_font = pygame.font.Font('font/game_plan/GamePlan - Dker.ttf', 50)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

bg_surface = pygame.image.load('bg/wallpaper.jpg').convert()

text_surface = test_font.render('Tracing Ladder Game', True, 'Blue')

player_surface = pygame.image.load('player/bug-64.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (player_surface.get_width(), player_surface.get_height()))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("white")

    screen.blit(bg_surface, (0,0))
    screen.blit(text_surface, (screen.get_width() / 2 - (text_surface.get_width() / 2), 10))
    pygame.draw.circle(screen, "orange", player_pos, 40)
    print(player_rect.left)
    screen.blit(player_surface, player_rect)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()