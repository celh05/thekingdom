#1 - import python libraries
import pygame
from pygame.locals import *
import math
import random

#2 - initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The Kingdom")
keys = [False, False, False, False]
playerPosition = [200,100]
pygame.mixer.init()

#3 - Load image
healthbar = pygame.image.load("resources/images/healthbar.png")
player = pygame.image.load("resources/images/player.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
#3.1 - Load audio
pygame.mixer.music.load("resources/audio/intro.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)

#4 - keep looping through the game
running = 1
exitcode = 0
while running:
	#badtimer -= 1

	#5 - clear game screen before drawing again
	screen.fill(0)

	#6 - draw the player on the screen at playerPosition
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))

	#6.1 - Set the player and rotation
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerPosition[1]+32), position[0]-playerPosition[0]+26)
	playerRotation = pygame.transform.rotate(player,0)
	playerPosition1 = (playerPosition[0]-playerRotation.get_rect().width/2, playerPosition[1]-playerRotation.get_rect().height/2)
	screen.blit(playerRotation,playerPosition1)
	#draw health bar
	screen.blit(healthbar,(450,0))

	#7 - Update the game screen

	pygame.display.flip()
	#loop through the events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False
		if (pygame.key.get_pressed()[pygame.K_m] == 1):
			pygame.mixer.music.pause()
		elif (pygame.key.get_pressed()[pygame.K_u] == 1):
			pygame.mixer.music.play(-1,0.0)
	#move player
	if keys[0]:
		playerPosition[1] -= 5
	elif keys[2]:
		playerPosition[1] += 5
	elif keys[1]:
		playerPosition[0] -= 5
	elif keys[3]:
		playerPosition[0] += 5	

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	pygame.display.flip()
