from view import maze
from view import battle
from view import screen
from view import menu

from model.persist import maze_dao
from model.persist import DAO

from model import personagemFactory
from model import enemyFactory

class GameControl:
	def __init__(self):
		self.display = screen.Screen()	# instancia a tela
		self.display.start()
		self.maze_game = maze.Maze(self.display)		# view do labirinto
		self.initial_menu = menu.Menu(self.display)		# view do menu	
		self.factory_personagem = personagemFactory.PersonagemFactory()
		self.personagem = None
		self.factory_enemy = enemyFactory.EnemyFactory()

	def show_menu(self):
		option = self.initial_menu.show()
		option = option.split('|')
		self.personagem = self.factory_personagem.create_personagem(option[1])

		# cretae a first register in DB if is a new login
		db = DAO.Dao()
		db.saveOnDb(self.personagem.get_name())
		return option[0]

	def begin(self):
		choice = self.show_menu()
		
		if choice == 'new':
			self.start_game()

		elif choice == 'continue':
			db = DAO.Dao()
			continueObj = db.getSaveByName(self.personagem.get_name())
			
			if continueObj != None:
				self.maze_game.continue_game(continueObj)
			
			self.start_game()

		elif choice == 'exit':
			self.end_game()

	def start_game(self):
		while True:
			map_event = self.maze_game.free_walk()

			if map_event[0] == 'ENEMY':			# if is a enemy event
				if self.enemy_event(map_event[1]) == 'lose':
					return

			elif map_event == 'WINNER':
				self.win_game()
				return

			elif map_event == 'END':
				self.end_game()
				return

			elif map_event == 'SAVE':
				db = DAO.Dao()
				obj = maze_dao.MazeDAO(self.maze_game)
				db.saveGame(self.personagem.get_name(), obj.get_maze_obj())

	def enemy_event(self, enemyType):
		fight = battle.Fight(self.display)
		fight.start()
		
		#check enemy type and create
		if(enemyType == '1'):
			enemy = self.factory_enemy.create_SrBilugo()
		elif(enemyType == '2'):
			enemy = self.factory_enemy.create_piruleta()
		elif(enemyType == '3'):
			enemy = self.factory_enemy.create_rei_da_cacimbinha()

		#life Personagem
		fight.set_num_life(1, str(self.personagem.get_life()) +"/"+ str(self.personagem.get_max_life()))
		fight.set_life(1, self.personagem.get_percent_life())
		#name self.Personagem
		fight.set_player_name('hero', str(self.personagem.get_name()) + ' (lvl '+ str(self.personagem.get_level()) + ')')
		#life Enemy
		fight.set_num_life(2, str(enemy.get_life())+"/"+str(enemy.get_max_life()))
		fight.set_life(2, enemy.get_percent_life())
		#name Enemy
		fight.set_player_name('enemy', enemy.get_name())
		#loop Battle
		while True:
			key_event = fight.get_event()

			if key_event == 119:	#verify key and do something - 119 = 'w'
				#hero attack first								
				#enemy take damage and check dead
				if(enemy.take_damage(self.personagem.get_damage())):
					if(self.personagem.receive_XP(enemy.get_experience_reward())): #send XP to player
						#self.personagem.get_level() #retorna novo lvl da criança
						pass

					#add drop for player
					drop = enemy.get_drop()
					#IMPRIMA DROP -Item-
					self.personagem.receive_item(drop)

					fight.call_animation(1)	# call animation of an atack
					#life self.Personagem
					fight.set_num_life(1, str(self.personagem.get_life()) +"/"+ str(self.personagem.get_max_life()))
					fight.set_life(1, self.personagem.get_percent_life())
					#life Enemy
					fight.set_num_life(2, "0/"+str(enemy.get_max_life()))
					enemy = None		
					fight.end()
					break

				while not fight.call_animation(1):	# call animation of an atack
					pass

				#enemy's Attack
				#player take damage and check dead
				if(self.personagem.take_damage(enemy.get_damage())):
					while not fight.call_animation(2):	# call animation of an atack
						pass
						
					#life self.Personagem
					fight.set_num_life(1, "0/"+ str(self.personagem.get_max_life()))
					fight.set_life(1, 0)
					#name self.Personagem
					fight.set_player_name('hero', str(self.personagem.get_name()) + ' (lvl '+ str(self.personagem.get_level()) + ')')
					#life Enemy
					fight.set_num_life(2, str(enemy.get_life())+"/"+str(enemy.get_max_life()))
					fight.set_life(2, enemy.get_percent_life())
					#name Enemy
					fight.set_player_name('enemy', enemy.get_name())

					fight.end()
					fight.game_over()
					self.display.end()
					return 'lose'
				
				while not fight.call_animation(2):	# call animation of an atack
					pass

				#life self.Personagem
				fight.set_num_life(1, str(self.personagem.get_life()) +"/"+ str(self.personagem.get_max_life()))
				fight.set_life(1, self.personagem.get_percent_life())
				#life Enemy
				fight.set_num_life(2, str(enemy.get_life())+'/'+str(enemy.get_max_life()))
				fight.set_life(2, enemy.get_percent_life())

			if key_event == 27:
				fight.end()
				break

		return 'win'

	def win_game(self):
		self.maze_game.win()
		self.display.end()

	def end_game(self):
		print('Saindo...')
		self.display.end()