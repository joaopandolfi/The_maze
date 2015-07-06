import pygame
from pygame.locals import *
from view import screen

class Menu:
	def __init__(self, display):	
		# screen var
		self.DISPLAY_THREAD = display
		self.DISPLAY = self.DISPLAY_THREAD.get_display()
		self.fontObj = pygame.font.Font('freesansbold.ttf', 15)

	def show(self):
		fpsClock = pygame.time.Clock()
		fps = self.DISPLAY_THREAD.get_fps()
		playerName = ''
		white = (255, 255, 255)
		key = 0

		while True:
			type_event = self.DISPLAY_THREAD.get_event_type()
			
			if type_event == KEYDOWN:
				key = self.DISPLAY_THREAD.get_event()
				
				if key == K_BACKSPACE:
					playerName = playerName[:len(playerName)-1]

				elif key == 13:
					break

				else:
					playerName += chr(key)

			self.DISPLAY.fill(white)
			text_obj = self.fontObj.render('Digite seu nome: ' + playerName, True, (0,0,0), white)
			self.DISPLAY.blit(text_obj, (20, 20))
			pygame.display.update()
			fpsClock.tick(fps)

		menuImg = pygame.image.load('data/img/title.png')
		option_y = 390

		while True:
			key = self.DISPLAY_THREAD.get_event()
			
			if key == K_DOWN:
				if option_y == 476:
					option_y = 390
				else:
					option_y += 43

			elif key == K_UP:
				if option_y == 390:
					option_y = 476
				else:
					option_y -= 43

			elif key == 13:
				if option_y == 390:
					return 'new|' + playerName

				elif option_y == 476:
					return 'exit|' + playerName

				else:
					return 'continue|' + playerName

			self.DISPLAY.fill((255, 255, 255))
			self.DISPLAY.blit(menuImg, (0, 0))
			pygame.draw.circle(self.DISPLAY, (0,0,0), (325, option_y), 5, 0)
			pygame.display.update()
			fpsClock.tick(fps)