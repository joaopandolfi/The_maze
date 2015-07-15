#item utilizado pelo player
class Item():
	def __init__(self):
		#atributos
		self.name = ""
		self.effect = 0
		#TROCAR POR ENUM
		self.type_item = 0 #1 - arma, 2 - munição, 3 - usável, 4 - artefato
		self.equipped = False
		self.position = 0
	
	def create(self,name,type_item,effect):
		self.name = name
		self.effect = effect
		self.type_item = type_item
	
	def get_effect(self):
		return self.effect
		
	def equip(self):
		self.equipped = True
		
	def unequip(self):
		self.equipped = False
	
	#retorna se o item está equipado ou nao 
	def is_equipped(self):
		return self.equipped

	def set_position(self,position):
		self.position = position
	
	def get_position(self,position):
		return self.position
		
	def get_name(self):
		return self.name

