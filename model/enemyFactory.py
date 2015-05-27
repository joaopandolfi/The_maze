#incluo libs do jogo
from model import enemy
from model import itemFactory
#Fabrica de inimigos
class EnemyFactory():
	
	def __init__(self):
		self.item_factory = itemFactory.ItemFactory()
		self.enemy = enemy.Enemy()
	
	def create_MrSalaminho(self):
		self.enemy.set_name("Mr Salaminho (lvl 3)")
		self.enemy.set_level(3)
		self.enemy.recover_full_life()
		self.enemy.set_experience_reward(75)
		self.enemy.set_life_recover_mutiplier(1)
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_bakugan_bow())
		self.enemy.receive_item(self.item_factory.create_dart())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_low_health_potion())
		self.enemy.receive_item(self.item_factory.create_medium_health_potion())
		self.enemy.receive_item(self.item_factory.create_troll_health_potion())
		self.enemy.receive_item(self.item_factory.create_bakugan_bow())
		return self.enemy
		
	def create_SrBilugo(self):
		self.enemy.set_name("Sr Bilugo (lvl 1)")
		self.enemy.set_level(0)
		self.enemy.recover_full_life()
		self.enemy.set_experience_reward(30)
		self.enemy.set_life_recover_mutiplier(1)
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_simple_bow())
		self.enemy.receive_item(self.item_factory.create_brush())
		#equipo os itens
		#self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_low_health_potion())
		self.enemy.receive_item(self.item_factory.create_low_health_potion())
		self.enemy.receive_item(self.item_factory.create_medium_health_potion())
		self.enemy.receive_item(self.item_factory.create_troll_health_potion())
		self.enemy.receive_item(self.item_factory.create_simple_bow())
		return self.enemy
		
	def create_PAULUS(self):
		self.enemy.set_name("PAULUS POO2 Power (lvl 999)")
		self.enemy.set_level(5)
		self.enemy.recover_full_life()
		self.enemy.set_experience_reward(100)
		self.enemy.set_life_recover_mutiplier(2)
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.receive_item(self.item_factory.create_brush())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_OP_health_potion())
		self.enemy.receive_item(self.item_factory.create_OP_health_potion())
		self.enemy.receive_item(self.item_factory.create_OP_health_potion())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		return self.enemy
		
	def create_piruleta(self):
		self.enemy.set_name("Piruleta (lvl 2)")
		self.enemy.set_level(2)
		self.enemy.recover_full_life()
		self.enemy.set_experience_reward(40)
		self.enemy.set_life_recover_mutiplier(1)
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.receive_item(self.item_factory.create_medium_health_potion())
		return self.enemy
		
	def create_rei_da_cacimbinha(self):
		self.enemy.set_name("Rei da Cacimbinha (lvl 7)")
		self.enemy.set_level(7)
		self.enemy.recover_full_life()
		self.enemy.set_experience_reward(120)
		self.enemy.set_life_recover_mutiplier(3)
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_sexy_pistol())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_sexy_pistol())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		return self.enemy	
		
	def create_lepos_lepus(self):
		self.enemy.set_name("Lepos lepus (lvl 3)")
		self.enemy.set_level(3)
		self.enemy.recover_full_life()
		self.enemy.set_experience_reward(49)
		self.enemy.set_life_recover_mutiplier(2)
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.receive_item(self.item_factory.create_low_health_potion())
		return self.enemy
