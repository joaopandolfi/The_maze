#incluo libs do jogo
from model import enemyBuilder

class ReiDaCacimbinhaBuilder(enemyBuilder.EnemyBuilder):

	#construtor
	def __init__(self):
		super().__init__()

	#OVERRIDE

	def buildEnemy(self):
		self.enemy.set_name("Rei da Cacimbinha (lvl 7)")
		self.enemy.set_level(7)
		self.enemy.set_experience_reward(120)
		self.enemy.set_life_recover_mutiplier(3)
		super().buildEnemy()

	def buildItens(self):
		#coloco a arma e munição na Bag
		self.enemy.receive_item(self.item_factory.create_sexy_pistol())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		#equipo os itens
		self.enemy.equip_arma(0)
		self.enemy.equip_munition(1)

	def buildDrop(self):
		#itens dropaveis
		self.enemy.receive_item(self.item_factory.create_sexy_pistol())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
