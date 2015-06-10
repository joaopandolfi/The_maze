#importo libs do jogo
from model import enemyBuilder

#Diretor de inimigos
class DirectorEnemy():

    def __init__(self):
        self.enemyBuilder = None

    def setBuilder(self, enemyBuilder):
        self.enemyBuilder = enemyBuilder

    def createEnemy(self):
        #se estiver vazio, retorna nada
        if(self.enemyBuilder == None):
            return None

        #se n estiver vazio, construo o enemy
        self.enemyBuilder.buildEnemy()
        self.enemyBuilder.buildItens()
        self.enemyBuilder.buildDrop()

        #retorno o inimigo
        return self.enemyBuilder.getEnemy()
