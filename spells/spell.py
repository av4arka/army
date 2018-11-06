class Spell:


    def __init__(self, spell_power, cost):
        self._spell_power = spell_power
        self._cost = cost

    @property
    def spell_power(self):
        return self._spell_power

    @property
    def cost(self):
        return self._cost

    @spell_power.setter
    def spell_power(self, new_spell_power):
        self._spell_power = new_spell_power

    def test_combat_spells(self, attacker):
        if attacker.title != 'Wizard':
            self.spell_power /= 2

    def test_healing_spells(self, attacker):
        if attacker.title == 'Wizard':
            self._spell_power /= 2


        # void
        # Spell::testForHealingSpells(Unit * attacker)
        # {
        # if (strcmp(attacker->getTitle(), "Wizard") == 0 ) {
        #     setSpellPower(this->getSpellPower() / 2);
        # }
