from functions import ShowPlayerStats
from functions import ShowEnemyStats

from entities import enemy

##Cave 
enemies_cave = []

def cave():

    for i in range(3):

        Current_Enemy = enemy()
        enemies_cave.append(Current_Enemy)

        Current_Enemy.Name = "Goblin_"+(i+1)
        Current_Enemy.MaxHelth = 40
        Current_Enemy.Damage = 10


