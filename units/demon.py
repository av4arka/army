from units.unit import Unit
from exception.exception_unit import UnitIsDead

class Demon(Unit):


    def __init__(self, warlock, title='Demon', hit_points_limit=80, damage=30):
        Unit.__init__(self, title, hit_points_limit, damage)
        self._warlock = warlock

    def ensure_is_alive(self):
        if self.hit_points <= 0:
            self.hit_points = 0
            self.notify()
            self._warlock.demon_is_dead(self)
            raise UnitIsDead(self.title + ' is dead!')


    # def ensure_is_alive(self):
    #     void
    #     Demon::ensureIsAlive()
    #     {
    #     if (getHitPoints() <= 0)
    #     {
    #
    #         setHitPoints(0);
    #     warlock->eraseDemon(this);
    #     notify();
    #     throw
    #     UnitIsDead();
    #     }
    #     }
