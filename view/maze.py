import time
import pygame, sys
from pygame.locals import *

from view import maping
from view import player
from view import screen

class Maze():
	blurImg = pygame.image.load('data/img/blur.png')

	def __init__(self, display):	
		#self.background_x = 0
		#self.background_y = 0
		self.player = player.Player()
		self.map = maping.Map('map.txt')
		self.DISPLAY_THREAD = display
		self.DISPLAY = self.DISPLAY_THREAD.get_display()


	def menu(self):
		menuImg = pygame.image.load('data/img/title.png')
		option_y = 390

		while True:
			key = self.DISPLAY_THREAD.get_event()
			
			if key == 274:
				if option_y == 476:
					option_y = 390
				else:
					option_y += 43

			elif key == 273:
				if option_y == 390:
					option_y = 476
				else:
					option_y -= 43

			elif key == 13:
				return option_y

			self.DISPLAY.fill((255, 255, 255))
			self.DISPLAY.blit(menuImg, (0, 0))
			pygame.draw.circle(self.DISPLAY, (0,0,0), (325, option_y), 5, 0)
			pygame.display.update()

	def free_walk(self):
		#player_speed = 4
		fpsClock = pygame.time.Clock()

		while True:
			key = self.DISPLAY_THREAD.get_event()

			if key == 275:
				self.player.set_animation('right')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'right')

				if temp_event == ' ':
					self.player.j += 1
					#self.background_y = 0
					#self.background_x = -player_speed

				elif temp_event == '1' or temp_event == '2' or temp_event == '3':
					return ('I', temp_event)	# (event, type)

				elif temp_event == 'F':
					return ('F', 0)

			elif key == 276:
				self.player.set_animation('left')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'left')

				if temp_event == ' ':
					self.player.j -= 1
					#self.background_y = 0
					#self.background_x = player_speed

				elif temp_event == '1' or temp_event == '2' or temp_event == '3':
					return ('I', temp_event)	# (event, type)

				elif temp_event == 'F':
					return ('F', 0)

			elif key == 274:
				self.player.set_animation('down')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'down')
				
				if temp_event == ' ':
					self.player.i += 1
					#self.background_x = 0
					#self.background_y = -player_speed

				elif temp_event == '1' or temp_event == '2' or temp_event == '3':
					return ('I', temp_event)	# (event, type)

				elif temp_event == 'F':
					return ('F', 0)

			elif key == 273:
				self.player.set_animation('up')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'up')

				if temp_event == ' ':
					self.player.i -= 1
					#self.background_x = 0
					#self.background_y = player_speed

				elif temp_event == '1' or temp_event == '2' or temp_event == '3':
					return ('I', temp_event)	# (event, type)

				elif temp_event == 'F':
					return ('F', 0)

			else:
				self.player.set_animation('center')

			#self.map.move_map(self.background_x, self.background_y)
			#self.map.print_map(self.DISPLAYSURF)

			self.DISPLAY.fill((0,0,0))
			self.map.print_upper_part_map(self.DISPLAY)
			self.player.print_player(self.DISPLAY)
			self.map.print_lower_part_map(self.DISPLAY)
			#self.DISPLAYSURF.blit(self.blurImg, (0,0))

			pygame.display.update()
			fpsClock.tick(self.DISPLAY_THREAD.get_fps())

	def win(self):
		winImg = pygame.image.load('data/img/win.png')
		self.DISPLAY.blit(winImg, (0, 0))
		pygame.display.update()
		time.sleep(5)