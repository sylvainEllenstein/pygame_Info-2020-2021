#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:34:46 2021

@author: userlfa
"""

# Retrouver les touches

import pygame
import time

pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True
backgroundColor = (255, 255, 255)

class rectSprite():
	def __init__(self, rects, x, y):
		self.rects = rects # type : [[x, y, widht, height, color_tuple], ...]
		# --> pygame.rect object docs : https://www.pygame.org/docs/ref/rect.html#pygame.Rect
		# all rects are filled
		self.position = [x, y]
		
	def drawSprite(self, surface=screen):
		for x, y, width, height, color_tuple in self.rects : 
			pygame.draw.rect(surface, color_tuple, (x + self.position[0], y + self.position[1], width + self.position[1], height + self.position[1]))
	
	def clearSprite(self, surface=screen):
		for x, y, width, height, colorIgnored in self.rects :
			pygame.draw.rect(surface, backgroundColor, (x + self.position[0], y + self.position[1], width + self.position[1], height + self.position[1]))
		
	def moveSprite(self, vector):
		for i in (0, 1):
			self.position[i] += self.vector[i]
			
	def translateSprite(self, vector):
		self.clearSprite()
		self.moveSprite(vector)
		self.drawSprite()
		
def redraw(*sprites):
	# updates all positions of sprites on the surface screen
	screen.fill(backgroundColor)
	for sp in sprites :
		pass

"""
sprite1 = rectSprite([[0, 0, 50, 60, (0, 255, 0)], 
					   [12, 10, 10, 10, (255, 255, 255)]
					   [38, 10, ]])
"""

while running :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			running = False
	redraw()
	# affichage
	pygame.display.flip()

pygame.quit()