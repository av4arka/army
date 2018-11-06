from spells.lightning import Lightning
from spells.heal import Heal
from spells.blast import Blast
from spells.blessing import Blessing

class SpellBook:


    def __init__(self, spell):
        self._spell = spell
        self._spell_book = [Lightning(), Heal(),
                            Blast(), Blessing()]

    def change_spell(self, spell_number):

        try:
            return self._spell_book[spell_number]
        except IndexError:
            print('Spell book does not have this spell!')