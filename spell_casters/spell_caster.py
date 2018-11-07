from units.unit import Unit
from states.magic_state import MagicState
from abilities.magic_abilitiy import MagicAbilitiy
from spells.lightning import Lightning
from spell_book.spell_book import SpellBook

class SpellCaster(Unit):


    def __init__(self, title, hit_points_limit, damage, mana_limit, spell=Lightning(10,10)):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._magic_state = MagicState(title, hit_points_limit, damage, mana_limit)
        self._spell = spell
        self._magic_abilitiy = MagicAbilitiy(self, self._spell)
        self._spell_book = SpellBook(self._spell)

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

    def change_spell(self, spell_number):
        self._spell = self._spell_book.change_spell(spell_number)

    def change_abilitiy(self, new_abilitiy):
        super(SpellCaster, self).change_abilitiy(new_abilitiy)
        self._magic_abilitiy = new_abilitiy

    def change_state(self, new_state):
        super(SpellCaster, self).change_state(new_state)

        self._magic_state = new_state

    def __repr__(self):
        if self.title == 'Vampire' or 'Werewolf' or 'Wolf':
            return Unit.__repr__(self)
        return Unit.__repr__(self) + 'Mana: %d\n' % (self._magic_state.mana)