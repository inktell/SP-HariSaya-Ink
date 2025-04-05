import pygame
import random

WIDTH = 600
HEIGHT = 600
FPS = 30 # khung hinh tren giay

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Du lieu tu nguoi choi
    # Cap nhat thong so cua game
    # Ve cac doi tuong ra man hinh game
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (50, 50, 60, 60))
    pygame.draw.circle(screen, BLUE, (200,200), 75)
    pygame.display.flip()
    
pygame.quit()