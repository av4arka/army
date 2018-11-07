from abilities.abilitiy import Abilitiy

class PriestAbilitiy(Abilitiy):


    def __init__(self, attacker):
        Abilitiy.__init__(self, attacker)
        self._attacker = attacker

    def attack(self, enemy):
        damage_attacker = self._attacker.damage
        self._attacker.ensure_is_alive()

        if enemy.is_undead:
            damage_attacker *= 2

        enemy.take_damage(damage_attacker)
        if enemy.hit_points > 0:
            self.counter_attack(enemy)
