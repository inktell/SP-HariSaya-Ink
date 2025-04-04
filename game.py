import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mèo Bắt Chuột")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game clock
clock = pygame.time.Clock()

# Cat and mouse properties
cat_size = 50
mouse_size = 30
cat_speed = 3
mouse_speed = 5

# Initial positions
cat_x, cat_y = random.randint(0, WIDTH - cat_size), random.randint(0, HEIGHT - cat_size)
mouse_x, mouse_y = WIDTH // 2, HEIGHT // 2

# Cheese properties
cheese_size = 20
cheese_count = 5
cheeses = [
    (random.randint(0, WIDTH - cheese_size), random.randint(0, HEIGHT - cheese_size))
    for _ in range(cheese_count)
]

# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        mouse_y -= mouse_speed
    if keys[pygame.K_DOWN]:
        mouse_y += mouse_speed
    if keys[pygame.K_LEFT]:
        mouse_x -= mouse_speed
    if keys[pygame.K_RIGHT]:
        mouse_x += mouse_speed

    # Keep mouse within screen bounds
    mouse_x = max(0, min(WIDTH - mouse_size, mouse_x))
    mouse_y = max(0, min(HEIGHT - mouse_size, mouse_y))

    # Move cat randomly
    cat_x += random.choice([-cat_speed, cat_speed])
    cat_y += random.choice([-cat_speed, cat_speed])

    # Keep cat within screen bounds
    cat_x = max(0, min(WIDTH - cat_size, cat_x))
    cat_y = max(0, min(HEIGHT - cat_size, cat_y))

    # Check collision with cat
    if (cat_x < mouse_x + mouse_size and
        cat_x + cat_size > mouse_x and
        cat_y < mouse_y + mouse_size and
        cat_y + cat_size > mouse_y):
        score = 0  # Reset score if caught
        mouse_x, mouse_y = WIDTH // 2, HEIGHT // 2
        cat_x, cat_y = random.randint(0, WIDTH - cat_size), random.randint(0, HEIGHT - cat_size)

    # Check collision with cheese
    new_cheeses = []
    for cheese_x, cheese_y in cheeses:
        if (mouse_x < cheese_x + cheese_size and
            mouse_x + mouse_size > cheese_x and
            mouse_y < cheese_y + cheese_size and
            mouse_y + mouse_size > cheese_y):
            score += 1
        else:
            new_cheeses.append((cheese_x, cheese_y))
    cheeses = new_cheeses

    # If all cheeses are collected, spawn new ones
    if not cheeses:
        cheeses = [
            (random.randint(0, WIDTH - cheese_size), random.randint(0, HEIGHT - cheese_size))
            for _ in range(cheese_count)
        ]

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (cat_x, cat_y, cat_size, cat_size))
    pygame.draw.rect(screen, BLUE, (mouse_x, mouse_y, mouse_size, mouse_size))
    for cheese_x, cheese_y in cheeses:
        pygame.draw.rect(screen, YELLOW, (cheese_x, cheese_y, cheese_size, cheese_size))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()