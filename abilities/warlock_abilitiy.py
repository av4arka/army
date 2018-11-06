from abilities.abilitiy import Abilitiy
from units.demon import Demon

class WarlockAbilitiy(Abilitiy):
    max = 4

    def __init__(self, demons, warlock):
        Abilitiy.__init__(self, warlock)
        self._demons = demons
        self._warlock = warlock

    def use_abilitiy_two(self):
        if len(self._demons) >= WarlockAbilitiy.max:
            print('you can create maximum of four demons')
            return
        if self._warlock.mana < 20:
            print('too little mana!')
            return

        self._demons.append(Demon(self._warlock))
        self._warlock.expend_mana(20)
