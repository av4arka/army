from units.unit import Unit

class Soldier(Unit):


    def __init__(self, title, hit_points_limit, damage):
        Unit.__init__(self, title, hit_points_limit, damage)