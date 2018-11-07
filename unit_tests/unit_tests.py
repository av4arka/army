import unittest
from my_army import *
from exception.exception_unit import UnitIsDead

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
