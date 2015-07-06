import pygame, sys
from pygame.locals import *

# x and y like a Cartesian plane
# but start to grow from the top left corner of the screen

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
		'\n':pygame.image.load('data/img/empty.png'),
		'\r':pygame.image.load('data/img/empty.png')
	}

	__map_list = []
	__enemy_list = ['1','2','3','4','5','6','7','8','9']	# character enemy representation, add here for new enemys

	def __init__(self, path):
		self.__path = path
		self.txt_to_list()
		self.__map_matrix = self.get_map_matrix()

	def txt_to_list(self):	# this list is use to print the map
		arq = open(self.__path,'rt')
		content = arq.readline()
		line = 0
		column = 6 	# start the column in six to put the map at the center of screen

		while content != '':
			for c in content:
				self.__map_list.append(Map_element(line * 50, column * 40, self.__images[c], c))
				line += 1

			line = 0
			column += 1
			content = arq.readline()

		arq.close()

	def get_map_matrix(self):	# this matrix is use to control colision on the map
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

	# the player must appear above the map but the map part down him must appear above him
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
		for map_index in self.__map_list:
			map_index.pos_x += x
			map_index.pos_y += y

	def isPermitted(self, line, column, direction):
		move_x = 0
		move_y = 0

		if direction == 'right':
			column += 1
			move_x = -50

		elif direction == 'left':
			column -= 1
			move_x = 50

		elif direction == 'down':
			line += 1
			move_y = -40

		elif direction == 'up':
			line -= 1
			move_y = 40

		else:
			return ''

		if self.__map_matrix[line][column] == ' ':
			self.move_map(move_x, move_y)
			return 'empty'

		elif self.__map_matrix[line][column] == 'F':
			return 'win'

		elif self.__map_matrix[line][column] in self.__enemy_list:
			return 'enemy|' + self.__map_matrix[line][column]

		else:
			return ''

	def get_map_obj(self):
		return self.__map_list

	def set_map_list(self, listObj):
		if listObj == 'none':
			return

		mapList = listObj.split("&")
		mapList = mapList[:len(mapList) - 1]
		self.__map_list = []

		for element in mapList:
			mapElem = element.split("|")
			self.__map_list.append(Map_element(int(mapElem[1]), int(mapElem[2]), self.__images[mapElem[0]], mapElem[0]))