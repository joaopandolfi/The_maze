#incluo libs do jogo
from model import enemyBuilder

class LeposLepusBuilder(enemyBuilder.EnemyBuilder):

	#construtor
	def __init__(self):
		super().__init__()

	#OVERRIDE

	def buildEnemy(self):
		self.enemy.set_name("Lepos lepus (lvl 3)")
		self.enemy.set_level(3)
		self.enemy.set_experience_reward(49)
		self.enemy.set_life_recover_mutiplier(2)
		super().buildEnemy()

	def buildItens(self):
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)

	def buildDrop(self):
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.receive_item(self.item_factory.create_low_health_potion())
