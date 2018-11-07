from spells.spell import Spell

class Blessing(Spell):


    def __init__(self, spell_power=50, cost=25):
        Spell.__init__(self, spell_power, cost)

    def use_spell(self, attacker, target):
        self.test_healing_spells(attacker)
        target.add_hit_points(self.spell_power)