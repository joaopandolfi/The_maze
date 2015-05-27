from model import itemFactory
from model import personagem

#fabrica de personagens
class PersonagemFactory():
	
	def _init_(self):
		self.personagem = None
		
	def create_personagem(self,name):
		item_factory = itemFactory.ItemFactory()
		self.personagem = personagem.Personagem()
		self.personagem.create(name)
		#coloco a arma e munição na Bag
		self.personagem.receive_item(item_factory.create_bakugan_bow())
		self.personagem.receive_item(item_factory.create_dart())
		#equipo os itens
		self.personagem.equip_arma(0)
		self.personagem.equip_munition(1)
		return self.personagem

