class entity:
    def _init_(self, MaxHealth):
        self.Health = MaxHealth
        self.Alive = True

class player(entity):
    def _init_(self):
        self.L_Attack = 10
        self.H_Attack = 25
        self.Stamina = 100

class enemy(entity):
    def _init_(self, damage):
        self.Damage = damage