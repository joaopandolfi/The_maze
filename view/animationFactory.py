import pygame, sys
from pygame.locals import *

class AnimationFactory:
	def __init__(self):
		self.animation_list = {}
		self.animationBuilder()

	def animationBuilder(self):
		self.animation_list['ani1'] = [	# colocar nomes melhores
			pygame.image.load('data/animation/ani_1_1.png'),
			pygame.image.load('data/animation/ani_1_2.png'),
			pygame.image.load('data/animation/ani_1_3.png'),
			pygame.image.load('data/animation/ani_1_4.png'),
			pygame.image.load('data/animation/ani_1_5.png'),
			pygame.image.load('data/animation/ani_1_6.png'),
			pygame.image.load('data/animation/ani_1_7.png')
		]

		self.animation_list['ani2'] = [
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_1.png'), True, False),
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_2.png'), True, False),
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_3.png'), True, False),
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_4.png'), True, False),
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_5.png'), True, False),
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_6.png'), True, False),
			pygame.transform.flip(pygame.image.load('data/animation/ani_1_7.png'), True, False)
		]

	def get_animation(self, option):
		return self.animation_list[option]