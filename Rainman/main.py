#Пофиксить зарядку энергии

import pygame
import sys
import random
# from object import Object


obj_width = 50
obj_height = 50
obj_x = random.randint(10, 1000)
obj_y = 0


#рисование падающего объекта
def drawObj():
    global obj_height, obj_width, obj_x, obj_y
    if obj_y <= 720-50-obj_height:
        pygame.draw.rect(root,(255, 0, 0), (obj_x, obj_y, obj_width, obj_height))
        obj_y += 10
    else:
        obj_y = 0-obj_height

clock = pygame.time.Clock()

pygame.init()
root = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("")

walk = [
    pygame.image.load('sprites/1.png'),
    pygame.image.load('sprites/2.png'),
    pygame.image.load('sprites/3.png'),
    pygame.image.load('sprites/4.png'),
]

player_stand = pygame.image.load('sprites/1.png')

player_width = 40
player_height = 60
player_pos_x = 50
player_pos_y = 670 - player_height
speed = 3



run = True

anim_count = 0

def draw():
    global anim_count
    
    root.fill((255,255,255))
    pygame.draw.rect(root, (0,110,180), (0, 720-50, 1300, 50))

    drawObj()
    
    # obj = Object(random.randint(10, 1000), 0, 10, 'sprites/object.png')

    # pygame.blit(obj.sprt(), (obj.x(), obj.y()))
    # obj.y_pos += obj.speed

    if anim_count +1 >= 20:
        anim_count = 0
    
    if going:
        root.blit(walk[anim_count//5], (player_pos_x, player_pos_y))
        anim_count += 1
    else:
        root.blit(player_stand, (player_pos_x, player_pos_y))


    pygame.display.update()

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        sys.exit()


    if keys[pygame.K_LSHIFT]:
        speed = 10
    else:
        speed = 4
    
    if keys[pygame.K_LEFT] and player_pos_x > 2:
        player_pos_x -= speed
        going = True
    elif keys[pygame.K_RIGHT] and player_pos_x < 1279 - player_width:
        player_pos_x += speed     
        going = True
    else:
        going = False
        anim_count = 0
    draw()



