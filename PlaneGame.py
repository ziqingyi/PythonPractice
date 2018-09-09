# -*- coding:utf- -*-

import pygame
import time
from pygame.locals import *
import random

class HeroPlane(object):
	def __init__(self,screen_temp):
		self.x = 210
		self.y = 700
		self.screen = screen_temp
		self.image=pygame.image.load("./pic/hero1.png")
		self.bullet_list = [] #store bullet object

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()

			if bullet.judge(): # check the border of the screen
				self.bullet_list.remove(bullet)

	def move_left(self):
		self.x -= 10
	def move_right(self):
		self.x += 10

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(object):
	def __init__(self,screen_temp):
		self.x = 0
		self.y = 0
		self.screen = screen_temp
		self.image=pygame.image.load("./pic/enemy0.png")

		self.direction = "right"

		self.bullet_list = [] #store bullet object

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
			if bullet.judge(): # check the border of the screen
				self.bullet_list.remove(bullet)

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
			






class Bullet(object):
	def __init__(self, screen_temp, x,y):
		self.x = x+40
		self.y = y-20
		self.screen = screen_temp
		self.image = pygame.image.load("./pic/bullet.png")
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
	def move(self):
		self.y-=10

	def judge(self): # check whether the bullet is out of screen

		if self.y<0:
			return True
		else:
			return False


class EnemyBullet(object):
	def __init__(self, screen_temp, x,y):
		self.x = x+24
		self.y = y+30
		self.screen = screen_temp
		self.image = pygame.image.load("./pic/bullet1.png")
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
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










