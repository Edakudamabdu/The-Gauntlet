# parent class
class entity:
    def __init__(self, MaxHealth):
        self.Health = MaxHealth
        self.Alive = True

# player class (dervied from entity class)
class player(entity):
    def __init__(self):

        super().__init__(100)

        self.Name = "Player 1"
        self.L_Attack = 10
        self.H_Attack = 25
        self.Stamina = 100
        self.Mana = 50

# enemy class skeletal
class enemy(entity):
    def __init__(self, MaxHealth, Damage):

        super().__init__(MaxHealth)

        self.Damage = Damage