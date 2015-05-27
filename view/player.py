import pygame, sys
from pygame.locals import *

class Player:
	def __init__(self):
		self.i = 0
		self.j = 8
		self.__pos_x = 410
		self.__pos_y = 245
		self.__animation = 0
		self.__animation_index = 1

		self.playerImg = {
			1 :  pygame.image.load('data/img/soldier/soldier (1).png'),
			2 :  pygame.image.load('data/img/soldier/soldier (2).png'),
			3 :  pygame.image.load('data/img/soldier/soldier (3).png'),
			4 :  pygame.image.load('data/img/soldier/soldier (4).png'),
			5 :  pygame.image.load('data/img/soldier/soldier (5).png'),
			6 :  pygame.image.load('data/img/soldier/soldier (6).png'),
			7 :  pygame.image.load('data/img/soldier/soldier (7).png'),
			8 :  pygame.image.load('data/img/soldier/soldier (8).png'),
			9 :  pygame.image.load('data/img/soldier/soldier (9).png'),
			10 : pygame.image.load('data/img/soldier/soldier (10).png'),
			11 : pygame.image.load('data/img/soldier/soldier (11).png'),
			12 : pygame.image.load('data/img/soldier/soldier (12).png'),
			13 : pygame.image.load('data/img/soldier/soldier (13).png'),
			14 : pygame.image.load('data/img/soldier/soldier (14).png'),
			15 : pygame.image.load('data/img/soldier/soldier (15).png'),
			16 : pygame.image.load('data/img/soldier/soldier (16).png')
		}

	def update(self):
		if self.__animation == 1:	# down
			if self.__animation_index == 4:
				self.__animation_index = 1
			else:
				self.__animation_index += 1

		elif self.__animation == 2:	# left
			if self.__animation_index == 8:
				self.__animation_index = 5
			else:
				self.__animation_index += 1

		elif self.__animation == 3:	# right
			if self.__animation_index == 12:
				self.__animation_index = 9
			else:
				self.__animation_index += 1

		elif self.__animation == 4:	# up
			if self.__animation_index == 16:
				self.__animation_index = 13
			else:
				self.__animation_index += 1

	def set_animation(self, ani_type):
		if ani_type == 'left':
			self.__animation = 2
			self.__animation_index = 5

		elif ani_type == 'right':
			self.__animation = 3
			self.__animation_index = 9

		elif ani_type == 'up':
			self.__animation = 4
			self.__animation_index = 13

		elif ani_type == 'down':
			self.__animation = 1
			self.__animation_index = 1

		elif ani_type == 'center':
			self.__animation = 0
			self.__animation_index = 1

	def print_player(self, display):
		self.update()
		display.blit(self.playerImg[self.__animation_index], (self.__pos_x, self.__pos_y))
