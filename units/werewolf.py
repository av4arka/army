from units.unit import Unit
from abilities.werewolf_abilitiy import WerewolfAbilitiy
from states.werewolf_state import WerewolfState

class Werewolf(Unit):


    def __init__(self, title='Werewolf', hit_points_limit=170, damage=40):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._werewolf_state = WerewolfState(title, hit_points_limit, damage, self)
        self._werewolf_abilitiy = WerewolfAbilitiy(self, self._werewolf_state)

    def use_abilitiy_one(self, target):
        self._werewolf_abilitiy.use_abilitiy_one(target)

    def use_abilitiy_two(self):
        self._werewolf_abilitiy.use_abilitiy_two()

    def take_magic_damage(self, damage):
        self._werewolf_state.take_magic_damage(damage)
