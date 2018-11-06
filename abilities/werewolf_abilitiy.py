from abilities.abilitiy import Abilitiy
from states.werewolf_state import WerewolfState

class WerewolfAbilitiy(Abilitiy):

    def __init__(self, attacker, werewolf_state):
        Abilitiy.__init__(self, attacker)
        self._attacker = attacker
        self._werewolf_state = werewolf_state
        self._not_transformed = ['Vampire', 'Werewolf', 'Demon']

    def use_abilitiy_one(self, target):
        for unit in self._not_transformed:
            if target.title == unit:
                print(unit, 'can\'t be bitten')
                return

        if self._werewolf_state.is_it_wolf():
            return

        target.change_state(WerewolfState(target.title, target.hit_points, target.damage, target))
        target.change_abilitiy(WerewolfAbilitiy(target, target.default_state))

        target.title = self._attacker.title
        target.hit_points_limit = self._attacker.hit_points_limit
        target.damage = self._attacker.damage

    def use_abilitiy_two(self):
        self._attacker.ensure_is_alive()

        if not self._werewolf_state.is_it_wolf():
            add_hit_points = self._attacker.hit_points_limit / 3
            wolf_hit_points = self._attacker.hit_points_limit + int(add_hit_points)
            wolf_damage = self._attacker.damage + 25

            self._attacker.title = 'Wolf'
            self._attacker.hit_points_limit = wolf_hit_points
            self._attacker.damage = wolf_damage

            self._werewolf_state.change_state_wolf()
        else:
            diff_hit_points = self._attacker.hit_points_limit / 4
            werewolf_hit_points = self._attacker.hit_points_limit - int(diff_hit_points)
            werewolf_damage = self._attacker.damage - 25

            self._attacker.title = 'Werewolf'
            self._attacker.hit_points_limit = werewolf_hit_points
            self._attacker.damage = werewolf_damage

            self._werewolf_state.change_state_wolf()

