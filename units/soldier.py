from units.unit import Unit

class Soldier(Unit):


    def __init__(self, title='Soldier', hit_points_limit=200, damage=45):
        Unit.__init__(self, title, hit_points_limit, damage)