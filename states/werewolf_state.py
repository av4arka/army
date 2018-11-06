from states.default_state import DefaultState

class WerewolfState(DefaultState):


    def __init__(self, title, hit_points_limit, damage, werewolf):
        DefaultState.__init__(self, title, hit_points_limit, damage, self)
        self._werewolf = werewolf
        self._is_wolf = False

    def take_magic_damage(self, damage):
        if self._is_wolf:
            damage += 15

        self._werewolf.take_damage(damage)

    def is_it_wolf(self):
        return self._is_wolf

    def change_state_wolf(self):
        self._is_wolf = not self._is_wolf