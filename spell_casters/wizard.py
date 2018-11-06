from spell_casters.spell_caster import SpellCaster

class Wizard(SpellCaster):


    def __init__(self, title, hit_points_limit, damage, mana_limit):
        SpellCaster.__init__(self, title, hit_points_limit, damage, mana_limit)