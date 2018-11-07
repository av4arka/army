from spells.spell import Spell

class Heal(Spell):


    def __init__(self, spell_power=30, cost=10):
        Spell.__init__(self, spell_power, cost)

    def use_spell(self, attacker, target):
        self.test_healing_spells(attacker)
        target.add_hit_points(self.spell_power)