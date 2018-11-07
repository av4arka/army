from abilities.abilitiy import Abilitiy

class MagicAbilitiy(Abilitiy):


    def __init__(self, attacker, spell):
        Abilitiy.__init__(self, attacker)
        self._attacker = attacker
        self._spell = spell

    def use_abilitiy_one(self, target):
        amount_mana = self._attacker.mana

        self._attacker.ensure_is_alive()
        target.ensure_is_alive()
        self._spell = self._attacker.spell

        if amount_mana >= self._spell.cost:
            self._spell.use_spell(self._attacker, target)
            self._attacker.expend_mana(self._spell.cost)
