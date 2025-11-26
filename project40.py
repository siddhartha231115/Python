import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("two rectangles with controls")
white = (255, 255, 255)
red   = (255, 0, 0)
blue  = (0, 100, 255)
clock = pygame.time.Clock()
fps = 60
player_width, player_height = 50, 50
player_x, player_y = 100, 100
player_speed = 5
enemy_width, enemy_height = 50, 50
enemy_x, enemy_y = 500, 300
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    player_x = max(0, min(width - player_width, player_x))
    player_y = max(0, min(height - player_height, player_y))
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.flip()
pygame.quit()
sys.exit()