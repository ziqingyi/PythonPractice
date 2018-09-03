# -*- coding:utf- -*-

import pygame
import time

def main():

	#1. create window
	screen= pygame.display.set_mode((480,852),0,32)

	#2. create a background picture
	background = pygame.image.load("./pic/background.png")

	#3. create a plan picture
	hero = pygame.image.load("./pic/hero1.png")

	while True:

		screen.blit(background,(0,0))

		screen.blit(hero,(230,700))

		pygame.display.update()

		#time.sleep(5)


if __name__ == "__main__":
	main()










