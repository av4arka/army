from spell_casters.spell_caster import SpellCaster

class Wizard(SpellCaster):


    def __init__(self, title='Wizard', hit_points_limit=130, damage=10, mana_limit=100):
        SpellCaster.__init__(self, title, hit_points_limit, damage, mana_limit)