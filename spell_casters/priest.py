from spell_casters.spell_caster import SpellCaster
from spells.heal import Heal

class Priest(SpellCaster):


    def __init__(self, title='Priest', hit_points_limite=95, damage=17, mana_limit=85):
        SpellCaster.__init__(self, title, hit_points_limite, damage, mana_limit, Heal())