import pygame
import sys
import random
from tkinter import messagebox, Tk



obj_width = 50
obj_height = 50
obj_x = random.randint(10, 1000)
obj_y = 0




clock = pygame.time.Clock()

pygame.init()
root = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rainman")

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

rain_count = 1

class Rain:
    def __init__(self):
        self.x = random.randint(100, 1200)
        self.y = -50
        self.speed = speed

    def move(self):
        if self.y <= 620:
            pygame.draw.rect(root,(255, 0, 0), (self.x, self.y, 50, 50))
            self.y += 10
        else:
            self.y = 0-50
            self.x = random.randint(100,1200)
            global rain_count
            rain_count += 1
            createRain(rain_array)
run = True

anim_count = 0

def createRain(array):
    global rain_count
    for i in range(rain_count):
        array.append(Rain())

def drawRain(array):
    for rain in array:
        rain.move()

def draw():
    global anim_count
    
    root.fill((255,255,255))
    pygame.draw.rect(root, (0,110,180), (0, 720-50, 1300, 50))
    drawRain(rain_array)


    if anim_count +1 >= 20:
        anim_count = 0
    
    if going:
        root.blit(walk[anim_count//5], (player_pos_x, player_pos_y))
        anim_count += 1
    else:
        root.blit(player_stand, (player_pos_x, player_pos_y))


    pygame.display.update()


rain_array = []
createRain(rain_array)
while run:
    if len(rain_array) > 1000:
        Tk().withdraw()
        messagebox.showerror("SystemError", "Ошибка\nНе хватает ресурсов системы")
        sys.exit()
        
    
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
    



