from states.default_state import DefaultState
from abilities.abilitiy import Abilitiy

class Unit:


    def __init__(self, title, hit_points_limit, damage):
        self._default_state = DefaultState(title, hit_points_limit, damage)
        self._abilitiy = Abilitiy(self)

    def __call__():
        print('Unit can\'t be created')

    def ensure_is_alive(self):
        return self._default_state.ensure_is_alive()

    @property
    def hit_points(self):
        return self._default_state.hit_points

    @property
    def hit_points_limit(self):
        return self._default_state.hit_points_limit

    @property
    def damage(self):
        return self._default_state.damage

    @property
    def title(self):
        return self._default_state.title

    @hit_points.setter
    def hit_points(self, new_hit_points):
        self._default_state.hit_points = new_hit_points

    @hit_points_limit.setter
    def hit_points_limit(self, new_hit_points_limit):
        self._default_state.hit_points_limit = new_hit_points_limit

    @damage.setter
    def damage(self, new_damage):
        self._default_state.damage = new_damage

    @title.setter
    def title(self, new_title):
        self._default_state.title = new_title


    def add_hit_points(self, heal):
        self._default_state.add_hit_points(heal)

    def take_damage(self, damage):
        self._default_state.take_damage(damage)

    def take_magic_damage(self, damage):
        self._default_state.take_magic_damage(damage)

    def attack(self, enemy):
        self._abilitiy.attack(enemy)

    def __repr__(self):
        return 'Title: %s\nHp: %d\nDmg: %d\n' % (self.title, self.hit_points, self.damage)


