from abilities.abilitiy import Abilitiy

class RoqueAbilitiy(Abilitiy):


    def __init__(self, attacker):
        Abilitiy.__init__(self, attacker)
        self._attacker = attacker

    def attack(self, enemy):
        self._attacker.ensure_is_alive()
        enemy.take_damage(self._attacker.damage)