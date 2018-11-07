from spell_casters.spell_caster import SpellCaster
from interfaces.observer import Observer
from abilities.necromancer_abilitiy import NecromancerAbilitiy
from exception.exception_unit import UnitIsDead

class Necromancer(SpellCaster, Observer):


    def __init__(self, title='Necromancer', hit_points_limit=130, damage=40):
        SpellCaster.__init__(self, title, hit_points_limit, damage, 0)
        self._necromancer_abilitiy = NecromancerAbilitiy(self)
        self._observables = []
        self._is_undead = True

    def ensure_is_alive(self):
        if self.hit_points <= 0:
            self.hit_points = 0

            for observable in self._observables:
                observable.detach(self)
            self.notify()
            raise UnitIsDead(self.title + 'is dead!')

    def attack(self, enemy):
        if self.title != 'Werewolf':
            self._necromancer_abilitiy.use_abilitiy_one(enemy)
        super(Necromancer, self).attack(enemy)

    def add_observable(self, observable):
        self._observables.append(observable)

    def erase_observable(self, observable):
        self._observables.remove(observable)

    def update(self, observable):
        heal = observable.hit_points_limit / 3


        self.erase_observable(observable)
        self.add_hit_points(int(heal))

    @property
    def is_undead(self):
        return self._is_undead

    def change_abilitiy(self, new_abilitiy):
        print()
        super(Necromancer, self).change_abilitiy(new_abilitiy)
        self._necromancer_abilitiy = new_abilitiy

        if self.title == 'Werewolf':
            self._is_undead = False

        for observable in self._observables:
            observable.detach(self)

        del self._observables
