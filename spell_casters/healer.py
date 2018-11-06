from spell_casters.spell_caster import SpellCaster
from spells.heal import Heal

class Healer(SpellCaster):


    def __init__(self, title='Healer', hit_points_limit=110, damage=15, mana_limit=90):
        SpellCaster.__init__(self, title, hit_points_limit, damage, mana_limit, Heal())