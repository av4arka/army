from units.unit import Unit
from abilities.roque_abilitiy import RoqueAbilitiy

class Roque(Unit):


    def __init__(self, title, hit_points_limit, damage):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._roque_abilitiy = RoqueAbilitiy(self)

    def attack(self, enemy):
        self._roque_abilitiy.attack(enemy)