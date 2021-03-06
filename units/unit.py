from abilities.abilitiy import Abilitiy
from states.default_state import DefaultState
from interfaces.observable import Observable

class Unit(Observable):

    def __init__(self, title, hit_points_limit, damage):
        if not self.valid_arguments(title, hit_points_limit, damage):
            raise ValueError

        self._default_state = DefaultState(title, hit_points_limit, damage, self)
        self._abilitiy = Abilitiy(self)
        self._observers = []

    def  valid_arguments(self, title, hit_points_limit, damage):
        if isinstance(hit_points_limit, int) and isinstance(damage, int) \
                and isinstance(title, str):
            return True
        return False

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

    @property
    def default_state(self):
        return self._default_state

    @property
    def is_undead(self):
        return False

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

    def take_damage(self, damage):
        self._default_state.take_damage(damage)

    def take_magic_damage(self, damage):
        self._default_state.take_magic_damage(damage)

    def attack(self, enemy):
        self._abilitiy.attack(enemy)

    def change_abilitiy(self, new_abilitiy):
        self._abilitiy = new_abilitiy

    def change_state(self, new_state):
        self._default_state = new_state

    def add_hit_points(self, heal):
        self._default_state.add_hit_points(heal)

    def use_abilitiy_one(self, target):
        self._abilitiy.use_abilitiy_one(target)

    def use_abilitiy_two(self):
        self._abilitiy.use_abilitiy_two()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def __repr__(self):
        return 'Title is %s\nHp: %d\nDmg: %d\n' % (self.title, self.hit_points, self.damage)


