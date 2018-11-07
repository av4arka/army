import unittest

from exception.exception_unit import UnitIsDead
from my_army.my_army import *


class SoldierTest(unittest.TestCase):

    def test_attack(self):
        soldier = Soldier()
        soldier2 = Soldier()

        soldier.attack(soldier2)
        self.assertEqual(soldier.hit_points, 177)
        self.assertEqual(soldier2.hit_points, 155)

    def test_vampire_use_abilitiy(self):
        soldier = Soldier()
        vampire = Vampire()

        vampire.use_abilitiy_one(soldier)
        self.assertEqual(soldier.hit_points_limit, vampire.hit_points_limit)
        self.assertLessEqual(vampire.hit_points_limit, soldier.hit_points_limit)
        self.assertEqual(soldier.damage, vampire.damage)

    def test_werewolf_use_abilitiy(self):
        soldier = Soldier()
        werewolf = Werewolf()

        werewolf.use_abilitiy_one(soldier)
        self.assertEqual(soldier.hit_points_limit, werewolf.hit_points_limit)
        self.assertLessEqual(werewolf.hit_points_limit, soldier.hit_points_limit)
        self.assertEqual(soldier.damage, werewolf.damage)

    def test_unit_is_dead(self):
        soldier = Soldier()
        roque = Roque()

        try:
            roque.attack(soldier)
            roque.attack(soldier)
            roque.attack(soldier)
            roque.attack(soldier)
            roque.attack(soldier)
        except UnitIsDead:
            self.assertEqual(soldier.hit_points, 0)

class BerserkerTest(unittest.TestCase):

    def test_take_magic_damage(self):
        berserker = Berserker()
        hp_berserker = berserker.hit_points

        berserker.take_magic_damage(40)
        self.assertEqual(berserker.hit_points, hp_berserker)

    def test_vampire_use_abilitiy(self):
        berserker = Berserker()
        vampire = Vampire()

        vampire.use_abilitiy_one(berserker)
        berserker.take_damage(40)
        self.assertEqual(berserker.hit_points_limit, vampire.hit_points_limit)
        self.assertNotEqual(berserker.hit_points, berserker.hit_points_limit)

    def test_werewolf_use_abilitiy(self):
        berserker = Berserker()
        werewolf = Werewolf()

        werewolf.use_abilitiy_one(berserker)
        berserker.take_magic_damage(40)

        self.assertEqual(berserker.hit_points, 130)
        self.assertEqual(werewolf.hit_points_limit, berserker.hit_points_limit)

        berserker.use_abilitiy_two()
        self.assertEqual(berserker.hit_points_limit, 226)

class RoqueTest(unittest.TestCase):

    def test_attack(self):
        roque = Roque()
        soldier = Soldier()

        roque.attack(soldier)
        self.assertEqual(roque.hit_points, roque.hit_points_limit)

    def test_vampire_use_abilitiy(self):
        roque = Roque()
        vampire = Vampire()

        vampire.use_abilitiy_one(roque)
        roque.attack(vampire)
        self.assertEqual(roque.hit_points, 100)

class VampireTest(unittest.TestCase):

    def test_attack(self):
        vampire1 = Vampire()
        vampire2 = Vampire()

        vampire1.attack(vampire2)
        self.assertEqual(vampire1.hit_points, 100)
        self.assertEqual(vampire2.hit_points, 83)
        vampire2.attack(vampire1)
        self.assertEqual(vampire1.hit_points, 53)
        self.assertEqual(vampire2.hit_points, 66)

class WerewolfTest(unittest.TestCase):

    def test_werewolf_use_abilitiy(self):
        werewolf = Werewolf()

        werewolf.use_abilitiy_two()
        self.assertEqual(werewolf.hit_points_limit, 226)
        self.assertEqual(werewolf.damage, 65)
        self.assertEqual(werewolf.title, 'Wolf')
        werewolf.use_abilitiy_two()
        self.assertEqual(werewolf.hit_points_limit, 170)
        self.assertEqual(werewolf.damage, 40)
        self.assertEqual(werewolf.title, 'Werewolf')

    def test_take_magic_damage(self):
        werewolf = Werewolf()

        werewolf.use_abilitiy_two()
        werewolf.take_magic_damage(40)
        self.assertEqual(werewolf.hit_points, 115)

class WizardTest(unittest.TestCase):

    def test_wizard_use_abilitiy(self):
        wizard = Wizard()
        soldier = Soldier()

        wizard.use_abilitiy_one(soldier)
        self.assertEqual(soldier.hit_points, 170)
        self.assertEqual(wizard.mana, 90)

    def test_do_mana(self):
        wizard = Wizard()

        wizard.expend_mana(40)
        self.assertEqual(wizard.mana, 60)
        wizard.add_mana(100)
        self.assertEqual(wizard.mana, 100)

    def test_change_spell(self):
        wizard = Wizard()
        soldier = Soldier()

        wizard.use_abilitiy_one(soldier)
        self.assertEqual(soldier.hit_points, 170)
        wizard.change_spell(1)
        wizard.use_abilitiy_one(soldier)
        self.assertEqual(soldier.hit_points, 185)
        wizard.change_spell(2)
        wizard.use_abilitiy_one(soldier)
        self.assertEqual(soldier.hit_points, 130)

class PriestTest(unittest.TestCase):

    def test_attack(self):
        priest = Priest()
        soldier = Soldier()
        vampire = Vampire()

        priest.attack(soldier)
        self.assertEqual(soldier.hit_points, 183)
        priest.attack(vampire)
        self.assertEqual(vampire.hit_points, 105)

class WarlockTest(unittest.TestCase):

    def test_warlock_use_abilitiy(self):
        warlock = Warlock()
        soldier = Soldier()
        vampire = Vampire()

        warlock.use_abilitiy_two()
        self.assertEqual(warlock[0].hit_points, 80)
        self.assertEqual(warlock[0].damage, 30)
        self.assertEqual(warlock.mana, 80)

        warlock[0].attack(soldier)
        self.assertEqual(soldier.hit_points, 170)
        self.assertEqual(warlock[0].hit_points, 57)

        try:
            soldier.attack(warlock[0])
            soldier.attack(warlock[0])
            soldier.attack(warlock[0])
        except UnitIsDead:
            self.assertEqual(warlock[0], None)

    def test_warlock_dead(self):
        warlock = Warlock()

        warlock.use_abilitiy_two()
        warlock.use_abilitiy_two()
        warlock.use_abilitiy_two()

        try:
            warlock.take_damage(150)
            warlock.take_damage(1)
        except:
            self.assertEqual(warlock[0], None)

class NecromancerTest(unittest.TestCase):

    def test_attack(self):
        necromancer = Necromancer()
        necromancer2 = Necromancer()
        soldier = Soldier()

        necromancer.attack(soldier)
        necromancer2.attack(soldier)

        try:
            soldier.take_damage(200)
            soldier.take_damage(1)
        except UnitIsDead:
            self.assertEqual(necromancer.hit_points, 130)
            self.assertEqual(necromancer2.hit_points, 130)

        necromancer.attack(necromancer2)
        try:
            necromancer2.take_damage(200)
            necromancer2.take_damage(1)
        except UnitIsDead:
            self.assertEqual(necromancer.hit_points, 130)

    def test_necromancer_dead(self):
        necromancer = Necromancer()
        soldier = Soldier()

        necromancer.attack(soldier)
        try:
            necromancer.take_damage(200)
            necromancer.take_damage(1)
        except UnitIsDead:
            self.assertEqual(necromancer.hit_points, 0)

        try:
            soldier.take_damage(200)
            soldier.take_damage(1)
        except UnitIsDead:
            self.assertEqual(necromancer.hit_points, 0)

    def test_werewolf_use_abilitiy(self):
        necromancer = Necromancer()
        werewolf = Werewolf()
        soldier = Soldier()

        necromancer.attack(werewolf)
        werewolf.use_abilitiy_one(necromancer)
        try:
            werewolf.take_damage(200)
            werewolf.take_damage(1)
        except UnitIsDead:
            self.assertEqual(necromancer.hit_points, 110)

        necromancer.attack(soldier)
        try:
            soldier.take_damage(200)
            soldier.take_damage(1)
        except UnitIsDead:
            self.assertEqual(necromancer.hit_points, 87)


if __name__ == '__main__':
    unittest.main()
