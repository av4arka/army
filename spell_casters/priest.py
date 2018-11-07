from spell_casters.spell_caster import SpellCaster
from abilities.priest_abilitiy import PriestAbilitiy
from spells.heal import Heal

class Priest(SpellCaster):


    def __init__(self, title='Priest', hit_points_limite=95, damage=17, mana_limit=85):
        SpellCaster.__init__(self, title, hit_points_limite, damage, mana_limit, Heal())
        self._priest_abilitiy = PriestAbilitiy(self)

    def attack(self, enemy):
        self._priest_abilitiy.attack(enemy)

    def change_abilitiy(self, new_abilitiy):
        super(Priest,self).change_abilitiy(new_abilitiy)
        self._priest_abilitiy = new_abilitiy