import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game Screen")
clock = pygame.time.Clock()

player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect(center=(400, 300))

SKY_BLUE = (50, 150, 255)

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
    
    screen.blit(player_image, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()