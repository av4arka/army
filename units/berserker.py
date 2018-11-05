from units.unit import Unit
from states.berserker_state import BerserkerState

class Berserker(Unit):


    def __init__(self, title, hit_points_limit, damage):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._berserker_state = BerserkerState(title, hit_points_limit, damage)

    def take_magic_damage(self, damage):
        self._berserker_state.take_magic_damage(damage)