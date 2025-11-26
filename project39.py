import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Basic Pygame Screen with Shapes and Text")
white = (255, 255, 255)
cyan = (0, 0, 0)
blue  = (0, 100, 255)
font = pygame.font.SysFont("Arial", 36)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    pygame.draw.rect(screen, blue, (100, 150, 200, 100))
    text_surface = font.render("hi my name is siddhartha!!!!!", True, cyan)
    screen.blit(text_surface, (100, 50))
    pygame.display.flip()