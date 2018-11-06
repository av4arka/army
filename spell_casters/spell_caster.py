from units.unit import Unit
from states.magic_state import MagicState
from abilities.magic_abilitiy import MagicAbilitiy
from spells.lightning import Lightning

class SpellCaster(Unit):


    def __init__(self, title, hit_points_limit, damage, mana_limit, spell=Lightning(10,10)):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._magic_state = MagicState(title, hit_points_limit, damage, mana_limit)
        self._spell = spell
        self._magic_abilitiy = MagicAbilitiy(self, self._spell)

    @property
    def mana(self):
        return self._magic_state.mana

    @property
    def mana_limit(self):
        return self._magic_state.mana_limit

    @property
    def spell(self):
        return self._spell

    def use_abilitiy_one(self, target):
        self._magic_abilitiy.use_abilitiy_one(target)

    def expend_mana(self, amount_mana):
        self._magic_state.expend_mana(amount_mana)

    def add_mana(self, amount_mana):
        self._magic_state.add_mana(amount_mana)

    def __repr__(self):
        return Unit.__repr__(self) + 'Mana: %d\n' % (self._magic_state.mana)