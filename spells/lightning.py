from spells.spell import Spell

class Lightning(Spell):


    def __init__(self, spell_power, cost):
        Spell.__init__(self, spell_power, cost)

    def use_spell(self, attacker, target):
        self.test_combat_spells(attacker)
        target.take_magic_damage(self.spell_power)
