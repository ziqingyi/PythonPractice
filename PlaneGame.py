# -*- coding:utf- -*-

import pygame
import time
from pygame.locals import *

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

	def move_left(self):
		self.x -= 10
	def move_right(self):
		self.x += 10

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))



class Bullet(object):
	def __init__(self, screen_temp, x,y):
		self.x = x+40
		self.y = y-20
		self.screen = screen_temp
		self.image = pygame.image.load("./pic/bullet.png")
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
	def move(self):
		self.y-=1




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


	while True:

		screen.blit(background,(0,0))

		hero.display()

		pygame.display.update()

		key_control(hero)


		time.sleep(0.01)


if __name__ == "__main__":
	main()










