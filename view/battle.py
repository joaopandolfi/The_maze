import threading
import time
import pygame, sys
from pygame.locals import *
from view import screen

class Fight(threading.Thread):
	event = 0
	COLOR = (255, 255, 255)
	__end = True
	animation = False
	animation_type = 0
	call_ani_again = True

	life_1 = 350
	life_2 = 350

	def __init__(self, display):
		threading.Thread.__init__(self)
		self.DISPLAY_THREAD = display
		self.DISPLAY = self.DISPLAY_THREAD.get_display()
		self.fontObj = pygame.font.Font('freesansbold.ttf', 15)
		self.life_1_obj = self.fontObj.render('100', True, (0,200,0) ,self.COLOR)
		self.life_2_obj = self.fontObj.render('100', True, (0,200,0) ,self.COLOR)

	def run(self):
		fpsClock = pygame.time.Clock()
		display_elements = [
			pygame.image.load('data/animation/ani_1_1.png')
		]

		while self.__end: # the main game loop
			self.event = self.DISPLAY_THREAD.get_event()

			if self.animation == True and self.animation_type != 0:
				self.do_animation()

			self.DISPLAY.fill(self.COLOR)

			for element in display_elements:
				self.DISPLAY.blit(element, (200, 300))

			pygame.draw.rect(self.DISPLAY, (0, 200, 0), (10, 10, self.life_1, 20))
			pygame.draw.rect(self.DISPLAY, (0, 200, 0), (790 - self.life_2, 10, self.life_2, 20))
			
			self.DISPLAY.blit(self.life_1_obj, (10, 40))
			self.DISPLAY.blit(self.life_2_obj, (750, 40))

			pygame.display.update()
			fpsClock.tick(self.DISPLAY_THREAD.get_fps())

	def call_animation(self, ani_type):
		if self.call_ani_again:
			self.animation = True
			self.animation_type = ani_type
			self.call_ani_again = False
			return True
		else:
			return False


	def do_animation(self):
		animation_sprite_list = []

		if self.animation_type == 1:
			animation_time = 0.3 # tempo em segundos da animação

			animation_sprite_list = [
				pygame.image.load('data/animation/ani_1_1.png'),
				pygame.image.load('data/animation/ani_1_2.png'),
				pygame.image.load('data/animation/ani_1_3.png'),
				pygame.image.load('data/animation/ani_1_4.png'),
				pygame.image.load('data/animation/ani_1_5.png'),
				pygame.image.load('data/animation/ani_1_6.png'),
				pygame.image.load('data/animation/ani_1_7.png')
			]

		elif self.animation_type == 2:
			animation_time = 0.3 # tempo em segundos da animação

			animation_sprite_list = [
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_1.png'), True, False),
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_2.png'), True, False),
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_3.png'), True, False),
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_4.png'), True, False),
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_5.png'), True, False),
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_6.png'), True, False),
				pygame.transform.flip(pygame.image.load('data/animation/ani_1_7.png'), True, False)
			]

		animation_time = animation_time / len(animation_sprite_list)

		for element in animation_sprite_list:
			self.DISPLAY.fill(self.COLOR)
			self.DISPLAY.blit(element, (200, 300))
			pygame.display.update()
			time.sleep(animation_time)

		self.animation = False
		self.animation_type = 0
		self.call_ani_again = True

	def get_event(self):
		temp_event = self.event
		self.event = 0
		return temp_event

	def set_life(self, life, modifier):	# modifier - percent
		if life == 1:
			self.life_1 = modifier * 350
		else:
			self.life_2 = modifier * 350

	def set_num_life(self, life, string):
		if life == 1:
			self.life_1_obj = self.fontObj.render(string, True, (0,200,0) ,self.COLOR)
		else:
			self.life_2_obj = self.fontObj.render(string, True, (0,200,0) ,self.COLOR)

	def game_over(self):
		loseImg = pygame.image.load('data/img/game_over.png')
		self.DISPLAY.blit(loseImg, (0, 0))
		pygame.display.update()
		time.sleep(5)

	def end(self):
		self.__end = False