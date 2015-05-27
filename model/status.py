#Classe que controla os Status do player
class Status():
	
	def __init__(self):
		self.level = 0
		self.life = 0
		self.alive = True
		self.aditional_damage = 0
		self.experience = 0
	
		#atributos que mudam de acordo com o level
		self.max_life = 10
		self.base_damage = 0
	
	#recupera vida toda
	def recover_full_life(self):
		self.life = self.max_life
		
	#recupera vida
	def recover_life(self,life):
		self.life += life
		if(self.life > self.max_life):
			self.life = self.max_life
	
	#recebe dano, Retorna True se o player morrer
	def take_damage(self,damage):
		self.life -= damage
		if(self.life <=0 ):
			self.alive = False
			self.live = 0
			return True
			
		#se não morreu
		return False

	#ganha XP, retorna True caso subiu de level
	def receive_XP(self,xp_received):
		#XP necessária para subir de level
		necessaryExperience = self.level*50 + 25
		#atualiza xp
		self.experience += int(xp_received)
		if(self.experience >= necessaryExperience):
			#atualizo a variável de xp caso haja excedente manter
			self.experience -= necessaryExperience
			self.level_up()
			return True
		
		#não subiu de level, retorna falso
		return False
	
	#sobe de level
	def level_up(self):
		#recalcula novo level
		self.set_level(self.level +1)
	
	#setters
	def set_level(self,level):
		self.level = level
		#calculo vida maxima
		self.max_life = level*5 + 25
		#calculo o dano base
		self.base_damage = level*2 + 1
	
	#dano adicional (proveniente de um item ou magia)
	def set_aditional_damage(self,aditional_damage):
		self.aditional_damage = aditional_damage
	
	#aumento dano adicional
	def add_aditional_damage(self,aditional):
		self.aditional_damage += aditional
	
	def rem_aditional_damage(self,aditional):
		self.aditional_damage = aditional
	
	def set_experience(self,xp):
		self.experience = xp
	
	#getters
	def is_alive(self):
		return self.alive

	def get_life(self):
		return self.life

	def get_max_life(self):
		return self.max_life

	def get_percent_life(self):
		return self.life / self.max_life
		
	def get_damage(self):
		return self.base_damage + self.aditional_damage
	
	def get_level(self):
		return self.level
			

