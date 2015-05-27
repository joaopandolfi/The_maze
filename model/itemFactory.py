#importo classes do jogo
from model import item

class ItemFactory():
	
	def __init__(self):
		self.item = None
	
	#ARMAS
	
	#1 - arma, 2 - munição, 3 - usável, 4 - artefato
	def create_simple_bow(self):
		self.item = item.Item()
		self.item.create("Arco simples [+3]",1,3) #nome,tipo,efeito
		return self.item
		
	def create_bakugan_bow(self):
		self.item = item.Item()
		self.item.create("Arco do Bakugan [+4]",1,4)
		return self.item

	def create_sexy_pistol(self):
		self.item = item.Item()
		self.item.create("Sexy Pistol [+10]",1,10)
		return self.item
		
	def create_estilingue(self):
		self.item = item.Item()
		self.item.create("Estilingue [+2]",1,2)
		return self.item

	def create_dart_pistol(self):
		self.item = item.Item()
		self.item.create("Pistola de dardos [+6]",1,6)
		return self.item

	#MUNIÇÕES
	
	def create_dart_poison(self):
		self.item = item.Item()
		self.item.create("Dardo envenenado [+2]",2,2)
		return self.item

	def create_dart(self):
		self.item = item.Item()
		self.item.create("Dardo [+1]",2,1)
		return self.item

	def create_holly_bullet(self):
		self.item = item.Item()
		self.item.create("Bala sagrada [+3]",2,3)
		return self.item

	def create_shit_monkey(self):
		self.item = item.Item()
		self.item.create("Bosta de macaco [+6]",2,6)
		return self.item

	def create_brush(self):
		self.item = item.Item()
		self.item.create("Pincel maroto [+1]",2,1)
		return self.item

	def create_paper_ball(self):
		self.item = item.Item()
		self.item.create("Bolinha de papel [+5]",2,5)
		return self.item

	#POTIONS
	
	def create_low_health_potion(self):
		self.item = item.Item()
		self.item.create("Pote de vida fraco [+3]",3,3)
		return self.item

	def create_medium_health_potion(self):
		self.item = item.Item()
		self.item.create("Pote de vida mahomenos [+6]",3,6)
		return self.item
	
	def create_OP_health_potion(self):
		self.item = item.Item()
		self.item.create("Pote de vida OVER POWER [+12]",3,12)
		return self.item

	def create_troll_health_potion(self):
		self.item = item.Item()
		self.item.create("Pote de vida suprize []",3,-5)
		return self.item
