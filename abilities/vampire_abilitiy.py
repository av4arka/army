from abilities.abilitiy import Abilitiy
from states.default_state import DefaultState

class VampireAbilitiy(Abilitiy):

    def __init__(self, attacker):
        Abilitiy.__init__(self, attacker)
        self._attacker = attacker
        self._not_transformed = ['Vampire', 'Werewolf', 'Demon']


    def attack(self, enemy):
        heal = enemy.hit_points_limit / 10
        self._attacker.ensure_is_alive()
        enemy.take_damage(self._attacker.damage)
        self._attacker.add_hit_points(heal)

        if enemy.hit_points > 0:
            self.counter_attack(enemy)

    def counter_attack(self, enemy):
        damage_enemy = enemy.damage / 2

        if enemy.title == 'Vampire':
            heal = self._attacker.hit_points_limit / 10

            enemy.add_hit_points(heal)
        self._attacker.take_damage(damage_enemy)

    def use_abilitiy_one(self, target):
        self._attacker.ensure_is_alive()
        target.ensure_is_alive()

        for unit in self._not_transformed:
            if target.title == unit:
                print(unit, 'can\'t be bitten')
                return

        target.change_abilitiy(VampireAbilitiy(target))
        target.change_state(DefaultState(target.title, target.hit_points, target.damage, target))

        target.title = self._attacker.title
        target.hit_points_limit = self._attacker.hit_points_limit
        target.damage = self._attacker.damage
