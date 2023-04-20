import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption('Red Ball')

clock = pygame.time.Clock()

x = 100
y = 100
change_x = 20
change_y = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= change_y
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += change_y
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= change_x
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += change_x

    
    if y > 500:
        y = 0
    if y < 0:
        y = 500
    if x > 700:
        x = 0
    if x < 0:
        x = 700  
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= change_y
    if pressed[pygame.K_DOWN]: y += change_y
    if pressed[pygame.K_LEFT]: x -= change_x
    if pressed[pygame.K_RIGHT]: x += change_x

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [x, y], 50)
    clock.tick(30)
    pygame.display.update()