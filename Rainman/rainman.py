import pygame
from pygame import transform
import random
from sys import platform
from os import system
from tkinter import messagebox, Tk


pygame.init()


scaling = False


class Rainman(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("sprites/1.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 660
		self.count = 1
		self.idle = pygame.image.load("sprites/1.png").convert_alpha()


	def moving(self):
		self.count += 1
		self.count = self.count % 4
		self.image = pygame.image.load('sprites/{}.png'.format(self.count + 1)).convert_alpha()

		
	def update(self):
		global scaling
		if scaling:
			self.image = pygame.transform.scale(self.image, (46, 120))
			self.rect.y = 600
		else:
			self.image = pygame.image.load('sprites/{}.png'.format(self.count + 1)).convert_alpha()
			self.rect.y = 660

		if is_move:
			if moving_right:
				if sprint:
					self.rect.x += 10
				else:
					self.rect.x += 4
			else:
				if sprint:
					self.rect.x -= 10
				else:
					self.rect.x -= 4
		else:
			if scaling:
				self.scaled_idle = self.idle
				self.image = pygame.transform.scale(self.scaled_idle, (43, 120))
			else:
				self.image = self.idle
	

class Raindrop(pygame.sprite.Sprite):
	def __init__(self, group):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('sprites/rain1.png')
		self.rect = self.image.get_rect()
		self.add(group)
		self.rect.x = random.randint(0, 1230)
		self.rect.y = -50

	def update(self):
		self.rect.y += 10
		if self.rect.y < 0:
			self.kill


 


size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

collision = False

man = Rainman()

weather = pygame.sprite.Group()
rainfall = Raindrop(weather)

moving_right = False
sprint = False

clock = pygame.time.Clock()

timer = 500

anim = pygame.USEREVENT + 1
pygame.time.set_timer(anim, 100)

rain = pygame.USEREVENT + 2
pygame.time.set_timer(rain, timer)

is_move = False


while True:
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		scaling = True
	if keys[pygame.K_b]:
		scaling = False

	if keys[pygame.K_ESCAPE]:
		exit()
	if keys[pygame.K_LSHIFT]:
		sprint = True
	
	else:
		sprint = False

	if keys[pygame.K_RIGHT]:
		moving_right = True
		is_move = True
	elif keys[pygame.K_LEFT]:
		moving_right = False
		is_move = True
	else:
		is_move = False

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()

		if event.type == anim:
			if is_move:
 				man.moving()

		if event.type == rain:
 			rainfall = Raindrop(weather)
 			pygame.time.set_timer(rain, timer)

	if timer > 10:
		timer -= 10
	
	if pygame.sprite.spritecollideany(man, weather):
		collision = True
	
	screen.fill((255, 255, 255))
	
	if not collision:
		man.update()
		weather.update()
	else:
		Tk().withdraw()
		messagebox.showerror("SystemError", "Ошибка\nЧто-то пошло не так...")
		break
	

	screen.blit(man.image, man.rect)
	weather.draw(screen)
	pygame.display.update()
	clock.tick(30)

if platform == 'linux' or platform == 'linux2':
    system('firefox pages/base.html')
elif platform == 'win32':
    system('start pages/base.html')
else:
    pass