import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game Screen")
clock = pygame.time.Clock()

SKY_BLUE = (50, 150, 255)
WHITE = (255, 255, 255)
RED = (255, 50, 50)

player_rect = pygame.Rect(375, 275, 50, 50)
circle_pos = [100, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5
    if keys[pygame.K_UP]: player_rect.y -= 5
    if keys[pygame.K_DOWN]: player_rect.y += 5

    screen.fill(SKY_BLUE)
    
    pygame.draw.rect(screen, WHITE, player_rect)
    pygame.draw.circle(screen, RED, circle_pos, 30)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()