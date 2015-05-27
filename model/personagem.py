#importo classes do jogo
from model import status
from model import bag
#PERSONAGEM DO JOGO
class Personagem():
	
	def __init__(self):
		#dados do player
		self.name = ""
		#variaveis de localização
		self.x_position = 0
		self.y_position = 0
		
		#Classes
		self.status = status.Status() #dados do player
		self.bag = bag.Bag() #mochila
		self.arma = None
		self.munition = None
	
	def create(self,name):
		self.set_name(name)
		self.set_position(0,0)
		self.set_level(0)
		self.recover_full_life()
	
	#define nome
	def set_name(self,name):
		self.name = name
	
	def get_name(self):
		return self.name
	
	#define posição
	def set_position(self,x,y):
		self.x_position = x
		self.y_position = y

	# ===== CONTROLE DE STATUS =====
	
	#recupera level
	def get_level(self):
		return self.status.get_level()

	#define level
	def set_level(self,level):
		self.status.set_level(level)
	
	#recebe o dano e retorna se morreu
	def take_damage(self,damage):
		return self.status.take_damage(damage)
		
	#recupera o dano do player
	def get_damage(self):
		return self.status.get_damage()	

	def get_life(self):
		return self.status.get_life()

	def get_max_life(self):
		return self.status.get_max_life()

	def get_percent_life(self):
		return self.status.get_percent_life()
	
	#ganha XP e sabe se subiu de level
	def receive_XP(self,xp):
		if(self.status.receive_XP(xp)):
			#subiu de level
			return True

	#recupera vida
	def recover_life(self,life):
		self.status.recover_life(life)
		
	#recupera vida toda
	def recover_full_life(self):
		self.status.recover_full_life()

	# ===== CONTROLE DE ITENS =====
		
	def receive_item(self,item):
		self.bag.add_item(item)
		
	def get_itens_bag(self):
		return self.bag.get_bag_itens()
		
	def get_equiped_itens(self):
		return self.bag.get_equiped_itens()
	
	#equipa arma
	def equip_arma(self,position):
		#se ja tinha alguma arma equipada
		if(self.arma != None):
			#removo o modificador da arma
			self.status.rem_aditional_damage(self.arma.get_effect())
		
		self.arma = self.bag.equip_item_position(position)
		#adiciono o modificador da arma
		self.status.add_aditional_damage(self.arma.get_effect())
		
	#desequipa arma
	def unequip_arma(self):
		if(self.arma != None):
			#removo status modificador
			self.status.rem_aditional_damage(self.arma.get_effect())
			#desequipo
			self.bag.unequip_item_position(self.arma.get_position())
			self.arma = None	
		
	#Equipa municao
	def equip_munition(self,position):	
		#se ja tinha alguma municao equipada
		if(self.munition != None):
			self.status.rem_aditional_damage(self.munition.get_effect())
		
		self.munition = self.bag.equip_item_position(position)
		#adiciono modificador da municao
		self.status.add_aditional_damage(self.munition.get_effect())
	
	#desequipa municao
	def unequip_munition(self):
		if(self.munition != None):
			#removo status modificador
			self.status.rem_aditional_damage(self.munition.get_effect())
			#desequipo
			self.bag.unequip_item_position(self.munition.get_position)
			self.munition = None
