# -*- coding:utf- -*-

import pygame
import time
from pygame.locals import *
import random

class Base(object):
	def __init__(self, screen_temp, x, y, image_name):
		self.x = x
		self.y = y
		self.screen = screen_temp
		self.image=pygame.image.load(image_name)

class BasePlane(Base):
	def __init__(self, screen_temp, x, y, image_name):
		Base.__init__(self, screen_temp, x, y, image_name)

		self.bullet_list = [] #store bullet object

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()

			if bullet.judge(): # check the border of the screen
				self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
	def __init__(self,screen_temp):
		BasePlane.__init__(self, screen_temp, 210, 700, "./pic/hero1.png")  # super().__init__() no self required.

	def move_left(self):
		self.x -= 10
	def move_right(self):
		self.x += 10

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
	def __init__(self,screen_temp):
		BasePlane.__init__(self, screen_temp, 0, 0, "./pic/enemy0.png")
		self.direction = "right"

	def move(self):

		if self.direction == "right":
			self.x += 5
		elif self.direction == "left":
			self.x -= 5

		if self.x > 430:
			self.direction = "left"
		elif self.x < 0:
			self.direction = "right"

	def fire(self):
		ranum = random.randint(1,100)
		if (ranum == 20 or ranum == 10):
			self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))
			
class BaseBullet(Base):

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
	def __init__(self, screen_temp, x,y):
		BaseBullet.__init__(self,screen_temp, x+40, y-20, "./pic/bullet.png")

	def move(self):
		self.y-=10

	def judge(self): # check whether the bullet is out of screen

		if self.y<0:
			return True
		else:
			return False


class EnemyBullet(BaseBullet):
	def __init__(self, screen_temp, x,y):
		BaseBullet.__init__(self,screen_temp, x+24, y+30, "./pic/bullet1.png")

	def move(self):
		self.y+=10

	def judge(self): # check whether the bullet is out of screen

		if self.y>852:
			return True
		else:
			return False




def key_control(hero_temp):
	#get the event, eg.Press button
	for event in pygame.event.get():
		#if press QUIT button
		if event.type == QUIT:
			print("exit")
			exit()
		#if press down button
		elif event.type == KEYDOWN:
			#if press a or left button
			if event.key == K_a or event.key ==K_LEFT:
				print('left')
				hero_temp.move_left()
			#if press d or right button
			elif event.key == K_d or event.key == K_RIGHT:
				print('right')
				hero_temp.move_right()
			#if press space 
			elif event.key == K_SPACE:
				print('space')
				hero_temp.fire()

def main():

	#1. create window
	screen= pygame.display.set_mode((480,852),0,32)

	#2. create a background picture
	background = pygame.image.load("./pic/background.png")

	#3. create a plan object
	hero = HeroPlane(screen)

	#4. create an enemy plane
	enemy = EnemyPlane(screen)


	while True:

		screen.blit(background,(0,0))

		hero.display()

		enemy.display()

		enemy.move()#move randomly by itself

		enemy.fire()

		pygame.display.update()

		key_control(hero)

		time.sleep(0.01)

if __name__ == "__main__":
	main()










