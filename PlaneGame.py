# -*- coding:utf- -*-

import pygame
import time
from pygame.locals import *

def main():

	#1. create window
	screen= pygame.display.set_mode((480,852),0,32)

	#2. create a background picture
	background = pygame.image.load("./pic/background.png")

	#3. create a plan picture
	hero = pygame.image.load("./pic/hero1.png")

	x = 210
	y = 700

	while True:

		screen.blit(background,(0,0))

		screen.blit(hero,(x,y))

		pygame.display.update()

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
				#if press d or right button
				elif event.key == K_d or event.key == K_RIGHT:
					print('right')
				#if press space 
				elif event.key == K_SPACE:
					print('space')




		time.sleep(0.01)


if __name__ == "__main__":
	main()










