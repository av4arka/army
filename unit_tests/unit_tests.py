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



if __name__ == '__main__':
    unittest.main()

