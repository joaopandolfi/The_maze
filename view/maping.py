import pygame, sys
from pygame.locals import *

class Map_element:
	def __init__(self, x, y, img, e_type):
		self.element_type = e_type
		self.img = img
		self.pos_x = x
		self.pos_y = y

class Map:
	__images = {
		'#':pygame.image.load('data/img/Wood_Block_Tall.png'),
		' ':pygame.image.load('data/img/Plain_Block.png'),
		'F':pygame.image.load('data/img/Plain_Block.png'),
		'1':pygame.image.load('data/img/enemies/Plain_Enemy1_Block.png'),
		'2':pygame.image.load('data/img/enemies/Plain_Enemy2_Block.png'),
		'3':pygame.image.load('data/img/enemies/Plain_Enemy3_Block.png'),
		'\n':pygame.image.load('data/img/empty.png')
	}

	__map_list = []

	def __init__(self, path):
		self.__path = path
		self.txt_to_list()
		self.__map_matrix = self.get_map_matrix()

	def txt_to_list(self):	# gambiarra
		arq = open(self.__path,'rt')
		content = arq.readline()
		i = 0
		j = 6

		while content != '':
			for c in content:
				self.__map_list.append(Map_element(i * 50, j * 40, self.__images[c], c))
				i += 1

			i = 0
			j += 1
			content = arq.readline()

		arq.close()

	def get_map_matrix(self):	# controle de colisão simplificado
		arq = open(self.__path,'rt')
		content = arq.readline()
		matrix = []
		line = []

		while content != '':
			for c in content:
				line.append(c)

			matrix.append(line)
			line = []
			content = arq.readline()

		arq.close()
		return matrix

	def print_map(self, display):
		for map_e in self.__map_list:
			if map_e.element_type == ' ':
				if map_e.pos_x < 850 and map_e.pos_x > -50 and map_e.pos_y > -85 and map_e.pos_y < 685:
					display.blit(map_e.img, (map_e.pos_x, map_e.pos_y))

	def print_upper_part_map(self, display):
		for map_e in self.__map_list:
				if map_e.pos_x < 850 and map_e.pos_x > -50 and map_e.pos_y > -85 and map_e.pos_y < 685:
					if map_e.pos_y > 245:
						break

					display.blit(map_e.img, (map_e.pos_x, map_e.pos_y))

	def print_lower_part_map(self, display):
		for map_e in self.__map_list:
				if map_e.pos_x < 850 and map_e.pos_x > -50 and map_e.pos_y > -85 and map_e.pos_y < 685:
					if map_e.pos_y < 245:
						continue

					display.blit(map_e.img, (map_e.pos_x, map_e.pos_y))

	def move_map(self, x, y):
		#flag = True
		# for map_index in self.__map_list:
		# 	if map_index.element_type == '#':
		# 		if map_index.pos_x + x + 50 > 400 and map_index.pos_x + x + 50 < 432:
		# 			flag = False

		# 		if map_index.pos_y + y + 40 > 250 and map_index.pos_y + y + 40 < 298:
		# 			flag = False
		#if flag:

		for map_index in self.__map_list:
			map_index.pos_x += x
			map_index.pos_y += y

	def isPermitted(self, i, j, direction):
		if direction == 'right':
			if self.__map_matrix[i][j + 1] == ' ':
				self.move_map( -50, 0)
			
			return self.__map_matrix[i][j + 1]

		elif direction == 'left':
			if self.__map_matrix[i][j - 1] == ' ':
				self.move_map( 50, 0)

			return self.__map_matrix[i][j - 1]

		elif direction == 'down':
			if self.__map_matrix[i + 1][j] == ' ':
				self.move_map( 0, -40)

			return self.__map_matrix[i + 1][j]

		elif direction == 'up':
			if self.__map_matrix[i - 1][j] == ' ':
				self.move_map( 0, 40)

			return self.__map_matrix[i - 1][j]