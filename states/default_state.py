from exception.exception_unit import UnitIsDead

class DefaultState:


    def __init__(self, title, hit_points_limit, damage):
        self._title = str(title)
        self._hit_points_limit = int(hit_points_limit)
        self._hit_points = int(hit_points_limit)
        self._damage = int(damage)

    def  ensure_is_alive(self):
        if self._hit_points <= 0:
            self._hit_points = 0
            raise UnitIsDead(self._title + ' is dead!')

    @property
    def hit_points(self):
        return self._hit_points

    @property
    def hit_points_limit(self):
        return self._hit_points_limit

    @property
    def damage(self):
        return self._damage

    @property
    def title(self):
        return self._title

    @hit_points.setter
    def hit_points(self, new_hit_points):
        if isinstance(new_hit_points, int):
            if new_hit_points > self._hit_points_limit:
                new_hit_points = self._hit_points_limit
            self._hit_points = new_hit_points

    @hit_points_limit.setter
    def hit_points_limit(self, new_hit_points_limit):
        if isinstance(new_hit_points_limit, int):
            if new_hit_points_limit < 0:
                new_hit_points_limit = 0
            if new_hit_points_limit < self._hit_points:
                self._hit_points = new_hit_points_limit
            self._hit_points_limit = new_hit_points_limit

    @damage.setter
    def damage(self, new_damage):
        if isinstance(new_damage, int):
            if new_damage <= 0:
                new_damage = 1
            self._damage = new_damage

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self._title = new_title

    def add_hit_points(self, heal):
        new_hit_points = self._hit_points + heal

        self.ensure_is_alive()
        if new_hit_points > self._hit_points_limit:
            new_hit_points = self._hit_points_limit

        self._hit_points = new_hit_points

    def take_damage(self, damage):
        self.ensure_is_alive()

        if damage < 0:
            damage = 0

        self._hit_points -= damage
        if self._hit_points < 0:
            self._hit_points = 0

    def take_magic_damage(self, damage):
        self.take_damage(damage)
