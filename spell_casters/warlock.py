from spell_casters.spell_caster import SpellCaster
from abilities.warlock_abilitiy import WarlockAbilitiy
from exception.exception_unit import UnitIsDead

class Warlock(SpellCaster):


    def __init__(self, title='Warlock', hit_points_limit=100, damage=10, mana_limit=100):
        SpellCaster.__init__(self, title, hit_points_limit, damage, mana_limit)
        self._demons = []
        self._warlock_abilitiy = WarlockAbilitiy(self._demons, self)

    def ensure_is_alive(self):
        if self.hit_points <= 0:
            self.hit_points = 0
            del self._demons
            raise UnitIsDead(self.title + 'is dead!')

    def use_abilitiy_two(self):
        self._warlock_abilitiy.use_abilitiy_two()

    def demon_is_dead(self, demon):
         self._demons.remove(demon)

    def __getitem__(self, item):
        try:
            return self._demons[item]
        except Exception:
            print('invalid index of demon!')

    def change_abilitiy(self, new_abilitiy):
        super(Warlock, self).change_abilitiy(new_abilitiy)
        self._warlock_abilitiy = new_abilitiy
        del self._demons

# void Warlock::ensureIsAlive() {
#     if ( getHitPoints() <= 0 ) {
#         setHitPoints(0);
#
#         for ( int lo = 0, hi = demons->size(); lo < hi; lo++ ) {
#             getDemon(lo)->notify();
#         }
#         demons->clear();
#         notify();
#         throw UnitIsDead();
#     }
# }