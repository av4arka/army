from abilities.abilitiy import Abilitiy

class NecromancerAbilitiy(Abilitiy):


    def __init__(self, attacker):
        Abilitiy.__init__(self, attacker)
        self._attacker = attacker

    def use_abilitiy_one(self, target):
        self._attacker.ensure_is_alive()
        target.ensure_is_alive()

        self._attacker.add_observable(target)
        target.attach(self._attacker)
