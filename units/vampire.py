from units.unit import Unit
from abilities.vampire_abilitiy import VampireAbilitiy

class Vampire(Unit):


    def __init__(self, title, hit_points_limit, damage):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._vampire_abilitiy = VampireAbilitiy(self)

    def attack(self, enemy):
        self._vampire_abilitiy.attack(enemy)

    def use_abilitiy_one(self, target):
        self._vampire_abilitiy.use_abilitiy_one(target)