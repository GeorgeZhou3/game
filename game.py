import pygame
import pygame.freetype
import gif_pygame
import random

lost = 0
pygame.init()
pygame.freetype.init()
title = pygame.freetype.SysFont('Calisto MT', 100, True, True)
subtitle = pygame.freetype.SysFont('Calibri', 30, True)
number = pygame.freetype.SysFont('Calibri', 30, True)
screen_width, screen_height = 802, 652
screen = pygame.display.set_mode((screen_width, screen_height))
lost = "Yourself"
pygame.display.set_caption("On Thin Ice")
grid = []
for x in range(36):
    grid.append([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
rot = []
for x in range(36):
    rot.append([])
    for i in range(27):
        rot[-1].append(random.randint(0,3)*90)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
face = 0
level = 1
def calcdir(x,y):
    dx = y[0] - x[0]
    dy = y[1] - x[1]
    
    if dy == 0:
        if dx > 0:
            return 180
        elif dx < 0:
            return 0
    
    elif dx == 0:
        if dy > 0:
            return 90
        elif dy < 0:
            return 270
ice3 = pygame.image.load('ice3.png')
ice2 = pygame.image.load('ice2.png')
ice1 = pygame.image.load('ice1.png')
pen2 = pygame.image.load('pen2.png')
pen1 = pygame.image.load('pen1.png')
#Gif loading
backgroundGif = gif_pygame.load("background.gif")
deathGif = gif_pygame.load("deadscreen.gif")
def randomx():
    global sprite_x, sprite_y, rec
    if random.randint(0,1):
        sprite_x = random.randint(0,26)
        if random.randint(0,1):
            sprite_y = 0
        else:
            sprite_y = 26
    else:
        sprite_y = random.randint(0,26)
        if random.randint(0,1):
            sprite_x = 0
        else:
            sprite_x = 26
    if (sprite_x, sprite_y) in [x[0] for x in rec]:
        randomx()
sprite_x = 12
sprite_y = 0

sprite_speed = 5
bullets = []
splash = pygame.mixer.Sound('splash.wav')
level = 0
step = 0
maxstep = 10
rec = []
number_of_sprites = 0
pygame.mixer.music.load('intro.wav')
pygame.mixer.music.play(loops=1, start=0.0)
#Animation tick
aTick = 0
while True:
    pygame.time.Clock().tick(60)
    print(aTick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if aTick >= 255:
        backgroundGif.render(screen, (0, 0))
        title.render_to(screen, (90, 90), "On Thin Ice", (0, 0, 0))
        subtitle.render_to(screen, (90, 180), "Press SPACE to start", (0, 0, 0))
        subtitle.render_to(screen, (90, 240), "Finish your steps without falling into water", (0, 0, 0))
        subtitle.render_to(screen, (90, 270), "or hitting another penguin", (0, 0, 0))
        subtitle.render_to(screen, (90, 300), "Use the arrow keys to move", (0, 0, 0))
        subtitle.render_to(screen, (90, 330), "The amount of steps required will increase by 10", (0, 0, 0))
        subtitle.render_to(screen, (90, 360), "every level, so be careful!", (0, 0, 0))
    else:
        aTick += 1
        screen.fill((255,255,255))
        title.render_to(screen, (90, 90), "Welcome to...", (0, 0, 0, aTick))


    keys = pygame.key.get_pressed()
    pygame.display.flip()

    if keys[pygame.K_SPACE]:
        break
        
    if keys[pygame.K_ESCAPE]:
        quit()
pygame.mixer.music.load('start.wav')
pygame.mixer.music.play(loops=1, start=0.0)
bTick = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.time.Clock().tick(60)
    if bTick >= 255:
        break
    bTick += 1
    screen.fill((0,0,0, bTick))
    title.render_to(screen, (90, 90), "Good luck!", (255, 255, 255))

    pygame.display.flip()
pygame.mixer.music.load('The winter castle.wav')
pygame.mixer.music.play(loops=-1, start=0.0)
moved = 0
lose = 0
while lose != 1:

    stopped = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    rec.append([])
    try:
        randomx()
    except:
        if random.randint(0,1):
            sprite_x = random.randint(0,26)
            if random.randint(0,1):
                sprite_y = 0
            else:
                sprite_y = 26
        else:
            sprite_y = random.randint(0,26)
            if random.randint(0,1):
                sprite_x = 0
            else:
                sprite_x = 26
    try:
        rec[-1].append((sprite_x,sprite_y))
    except:
        pass

    #for x in range(number_of_sprites):
    
    grid = []
    for x in range(36):
        grid.append([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
    

    
    while step < maxstep + 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if keys[pygame.K_ESCAPE]:
            quit()
        old_x = sprite_x
        old_y = sprite_y
        keys = pygame.key.get_pressed()
        if False and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]) and moved == 1:
            moved = 1
        else:
            keys = pygame.key.get_pressed()
            moved = 0
            if keys[pygame.K_LEFT] and moved != 1:
                moved = 1
                sprite_x -= 1
                face = 0
            if keys[pygame.K_RIGHT] and moved != 1:
                moved = 1
                sprite_x += 1
                face = 180
            if keys[pygame.K_UP] and moved != 1:
                moved = 1
                sprite_y -= 1
                face = 270
            if keys[pygame.K_DOWN] and moved != 1:
                moved = 1
                sprite_y += 1
                face = 90
            if moved == 1:
                
                dont = 0
                if sprite_x > 26 or sprite_x < 0:
                    dont = 1
                    sprite_x = old_x
                if sprite_y > 26 or sprite_y < 0:
                    dont = 1
                    sprite_y = old_y
                if dont == 0:
                    step += 1
                    rec[level].append((sprite_x, sprite_y))
                    grid[old_y][old_x] = grid[old_y][old_x] - 1
                if grid[sprite_y][sprite_x] < 1:
                    lose = 1
                    print("you dropped to water")
                    lost = "water"
                    splash.play()
                    break
                if dont == 0 and len(rec) > 1:
                    for x in rec[:-1]:
                        try:
                            cur = x[step-1]
                            grid[cur[1]][cur[0]] -= 1 
                        except:
                            pass
               
        screen.fill((0,0,255))
        
        for i in range(27):
            for j in range(27):
                
                if grid[j][i] == 3:
                    rotated_image = pygame.transform.rotate(ice3, rot[j][i])
                    screen.blit(rotated_image, ((i+1)*24-20, (j+1)*24-20))
                if grid[j][i] == 2:
                    rotated_image = pygame.transform.rotate(ice2, rot[j][i])
                    screen.blit(rotated_image, ((i+1)*24-20, (j+1)*24-20))
                if grid[j][i] == 1:
                    rotated_image = pygame.transform.rotate(ice1, rot[j][i])
                    screen.blit(rotated_image, ((i+1)*24-20, (j+1)*24-20))
        
        for j in range(len(rec)-1):
            i = rec[j]
            if not j in stopped:
                try:
                    try:
                        rotated_image = pygame.transform.rotate(pen2, calcdir(i[step-1], i[step]) )
                    except:
                        pass
                    cur = i[step] 
                    if grid[cur[1]][cur[0]]<1:
                        stopped.append(j)
                    screen.blit(rotated_image, ((cur[0]+1)*24-20, (cur[1]+1)*24-20)) 
                    if (cur[0]+1) == sprite_x+1 and (cur[1]+1) == sprite_y+1:
                        lose = 1
                        print("you hit another penguin")
                        lost = "penguin"
                        break
                except: 
                    try:
                        rotated_image = pygame.transform.rotate(pen2, calcdir(i[-2], i[-1]) )
                    except:
                        pass
                    cur = i[-1]
                    if grid[cur[1]][cur[0]]<1:
                        print("test")
                    screen.blit(rotated_image, ((cur[0]+1)*24-20, (cur[1]+1)*24-20)) 
                    if (cur[0]+1) == sprite_x+1 and (cur[1]+1) == sprite_y+1:
                        lose = 1
                        print("you hit another penguin")
                        lost = "penguin"
                        break
        if lose == 1:
            break
        rotated_image = pygame.transform.rotate(pen1, face)
        screen.blit(rotated_image, ((sprite_x+1)*24-20, (sprite_y+1)*24-20, 20, 20)) 
        number.render_to(screen, (652, 0), "Steps left:"+str(maxstep-step), (255, 255, 0))
        number.render_to(screen, (652, 30), "Score:"+str(level+1), (255, 255, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    level += 1
    step = 0
    maxstep += 10

aTick = 0
while True:
    aTick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if (aTick >= 80):
        screen.fill((255,255,255))
        title.render_to(screen, (90, 90), "you lost", (0, 0, 0))
        subtitle.render_to(screen, (90, 180), f"you lost to {lost}", (0, 0, 0))
        subtitle.render_to(screen, (90, 210), "Press ESC to end the game", (0, 0, 0))
    else:
        deathGif.render(screen, (0, 0))
    

    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

        
    if keys[pygame.K_ESCAPE]:
        quit()