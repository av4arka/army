from states.default_state import DefaultState

class MagicState(DefaultState):


    def __init__(self, title, hit_points_limit, damage, mana_limit):
        DefaultState.__init__(self, title, hit_points_limit, damage, self)
        self._mana_limit = mana_limit
        self._mana = mana_limit

    @property
    def mana(self):
        return self._mana

    @property
    def mana_limit(self):
        return self._mana_limit

    def expend_mana(self, amount_mana):
        new_amount_mana = self._mana - amount_mana

        if new_amount_mana < 0:
            new_amount_mana = 0

        self._mana = new_amount_mana

    def add_mana(self, amount_mana):
        new_amount_mana = self._mana + amount_mana

        if new_amount_mana > self._mana_limit:
            new_amount_mana = self.mana_limit

        self._mana = new_amount_mana
