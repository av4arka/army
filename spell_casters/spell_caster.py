from units.unit import Unit
from states.magic_state import MagicState

class SpellCaster(Unit):


    def __init__(self, title, hit_points_limit, damage, mana_limit):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._magic_state = MagicState(title, hit_points_limit, damage, mana_limit)

    @property
    def mana(self):
        return self._magic_state.mana

    @property
    def mana_limit(self):
        return self._magic_state.mana_limit

    def expend_mana(self, amount_mana):
        self._magic_state.expend_mana(amount_mana)

    def add_mana(self, amount_mana):
        self._magic_state.add_mana(amount_mana)

    def __repr__(self):
        return Unit.__repr__(self) + 'Mana: %d' % (self._magic_state.mana)