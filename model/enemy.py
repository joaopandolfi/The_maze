#incluo libs do jogo
from model import personagem
#inclui lib de random
import random

#inimigos
class Enemy(personagem.Personagem):

	#variaveis
	def __init__(self):
		super().__init__()
		self.damage = 0
		self.life_multiplier = 0
		self.experience_reward = 0
	
	# ==== COMBATE ====
	
	#executa uma ação retornando o dano a ser inflingido
	def get_action(self):
		choice = random.randint(1,10)
		#Escolha da ação
		if(choice == 1):
			#miss Attack
			self.damage = 0
		elif(choice == 2):
			#recupera vida
			self.recover_life(self.get_level()*self.life_multiplier)
			self.damage = 0
		else:
			#executa ataque comum
			self.damage = self.get_damage()
		
		return self.damage
	
	#define multiplicador para recuperar vida
	def set_life_recover_mutiplier(self,life_multiplier):
		self.life_multiplier = self.life_multiplier
	
	
	# ==== STATUS ====
	
	def set_experience_reward(self,experience):
		self.experience_reward = experience
		
	def get_experience_reward(self):
		return self.experience_reward
	
	# ==== ITENS ====
	
	#retorna um item para drop
	def get_drop(self):
		choice = random.randint(1,10)
		#30% de chance de dropar algo
		if(choice <= 3):
			itens = self.get_itens_bag()
			#retorna um item aleatorio
			choice = random.randint(0,len(itens)-1)
			return itens[choice]
			
		return None
		
