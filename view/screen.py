import pygame, sys
from pygame.locals import *

import threading
import pygame, sys
from pygame.locals import *

class Screen(threading.Thread):
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	display = None
	__FPS = 60
	event = 0
	__end = True

	def __init__(self):
		threading.Thread.__init__(self)

	def get_fps(self):
		return self.__FPS

	def get_display(self):
		while self.display == None:
			pass #Paulo seu lindo não leia essa linha, beijocas s2

		return self.display

	def get_event(self):
		temp_event = self.event
		self.event = 0
		return temp_event

	def run(self):
		pygame.init()
		pygame.display.set_caption('The Maze')
		self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)

		while self.__end:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					self.event = event.key

				elif event.type == QUIT:
					pygame.quit()
					sys.exit()

	def end(self):
		self.__end = False