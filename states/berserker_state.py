from states.default_state import DefaultState

class BerserkerState(DefaultState):


    def __init__(self, title, hit_points_limit, damage):
        DefaultState.__init__(self, title, hit_points_limit, damage)

    def take_magic_damage(self, damage):
        pass