import pygame
import pygame.freetype
import math

pygame.init()
pygame.freetype.init()
title = pygame.freetype.SysFont('Calisto MT', 100, True, True)
subtitle = pygame.freetype.SysFont('Calibri', 30, True)
screen_width, screen_height = 652, 652
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shadows")
grid = []
for x in range(36):
    grid.append([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
center = (360, 360)
def calc_start(step):
    deg = math.radians(30*(step-1)+270)
    return (300*math.cos(deg)+360,300*math.sin(deg)+360)
print(calc_start(1))
level = 1
start_pos = calc_start(level)
end_pos = calc_start((level+6)%12)
sprite_width, sprite_height = 50, 50
sprite_x = 12
sprite_y = 0
sprite_speed = 5
bullets = []
steps = 0
rec = []
number_of_sprites = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((255,255,255))
    title.render_to(screen, (90, 90), "Title", (0, 0, 0))
    subtitle.render_to(screen, (90, 180), "Press SPACE to start", (0, 0, 0))
    subtitle.render_to(screen, (90, 210), "Press ESC to quit", (0, 0, 0))
    subtitle.render_to(screen, (90, 240), "Go to the objective without getting hit", (0, 0, 0))
    subtitle.render_to(screen, (90, 270), "Use the arrow keys to move", (0, 0, 0))

    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    if keys[pygame.K_SPACE]:
        break
        
    if keys[pygame.K_ESCAPE]:
        quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    #for x in range(number_of_sprites):
    keys = pygame.key.get_pressed()
    old_x = sprite_x
    old_y = sprite_y
    if keys[pygame.K_LEFT] and moved != 1:
        moved = 1
        step += 1
        sprite_x -= 1
    if keys[pygame.K_RIGHT] and moved != 1:
        moved = 1
        step += 1
        sprite_x += 1
    if keys[pygame.K_UP] and moved != 1:
        moved = 1
        step += 1
        sprite_y -= 1
    if keys[pygame.K_DOWN] and moved != 1:
        moved = 1
        step += 1
        sprite_y += 1
    if sprite_x > 26 or sprite_x < 0:
        sprite_x = old_x
    if sprite_y > 26 or sprite_y < 0:
        sprite_y = old_y
    screen.fill(black)
    for i in range(27):
        for j in range(27):
            pygame.draw.rect(screen, (255,255,255), ((i+1)*24-20, (j+1)*24-20, 20, 20))
    pygame.draw.rect(screen, (0,0,0), ((sprite_x+1)*24-20, (sprite_y+1)*24-20, 20, 20))        
    pygame.display.flip()

    pygame.time.Clock().tick(60)
