#incluo libs do jogo
from model import enemy
from model import itemFactory

#builder de inimigos [abstract]
class EnemyBuilder():

    def __init__(self):
        self.enemy = enemy.Enemy()
        self.item_factory = itemFactory.ItemFactory()

    #crio metodos basicos do inimigo
    def buildEnemy(self):
        self.enemy.recover_full_life()

    #construo os itens do inimigo
    def buildItens(self):
        pass

    #construo o drop do inimigo
    def buildDrop(self):
        pass

    #retorno o inimigo
    def getEnemy(self):
        return self.enemy
