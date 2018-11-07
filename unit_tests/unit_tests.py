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

    def test_vampire_bite(self):
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



if __name__ == '__main__':
    unittest.main()


#     TEST_CASE("Test for Berserker")
#     {
#         Berserker
#     berserker;
#     int
#     hp = berserker.getHitPoints();
#     int
#     dmg = 10;
#
#     berserker.takeMagicDamage(dmg);
#     REQUIRE(berserker.getHitPoints() == hp);
#
#     SECTION("Vampire bite test")
#     {
#     Vampire
#     vampire;
#
#     vampire.useAbilitiy_1( & berserker);
#     hp = berserker.getHitPoints();
#     berserker.takeMagicDamage(dmg);
#     REQUIRE(berserker.getHitPointsLimit() == vampire.getHitPointsLimit());
#     REQUIRE(berserker.getHitPoints() == hp - dmg);
#
# }
#
# SECTION("Werewolf bite test")
# {
# Werewolf
# werewolf;
#
# werewolf.useAbilitiy_1( & berserker);
# hp = berserker.getHitPoints();
#
# berserker.takeMagicDamage(dmg);
# REQUIRE(berserker.getHitPoints() == hp - dmg);
#
# berserker.useAbilitiy_2();
# berserker.takeMagicDamage(dmg);
# REQUIRE(berserker.getHitPoints() == 191);
# }
# }
#
#
# TEST_CASE("Test for Roque")
# {
#     Roque
# roque;
# Soldier
# soldier;
# int
# hp = roque.getHitPoints();
#
# roque.attack( & soldier);
# REQUIRE(roque.getHitPoints() == hp);
#
# SECTION("Vampire bite test")
# {
# Vampire
# vampire;
#
# vampire.useAbilitiy_1( & roque);
# soldier.attack( & roque);
# REQUIRE(roque.getHitPoints() == 105);
# }
# }
#
#
# TEST_CASE("Test for Vampire")
# {
#     Vampire
# vampire;
# Vampire
# vampire2;
#
# vampire.attack( & vampire2);
# REQUIRE(vampire.getHitPoints() == 100);
# REQUIRE(vampire2.getHitPoints() == 83);
# vampire2.attack( & vampire);
# REQUIRE(vampire.getHitPoints() == 53);
# REQUIRE(vampire2.getHitPoints() == 66);
# }
#
#
# TEST_CASE("Test for Werewolf")
# {
#     Werewolf
# werewolf;
#
# SECTION("Transmutation")
# {
# int
# addHp = werewolf.getHitPointsLimit() / 3;
# int
# newHp = werewolf.getHitPoints() + addHp;
# int
# newDmg = werewolf.getDamage() + 25;
# int
# returnLives = newHp / 4;
#
# werewolf.useAbilitiy_2();
# REQUIRE(werewolf.getHitPointsLimit() == newHp);
# REQUIRE(werewolf.getDamage() == newDmg);
# werewolf.useAbilitiy_2();
# REQUIRE(werewolf.getHitPointsLimit() == newHp - returnLives);
# REQUIRE(werewolf.getDamage() == newDmg - 25);
# }
#
# SECTION("Test on take magic damage")
# {
# int
# hitPoints = werewolf.getHitPoints();
# int
# dmg = 20;
#
# werewolf.takeMagicDamage(dmg);
# REQUIRE(werewolf.getHitPoints() == hitPoints - dmg);
#
# werewolf.useAbilitiy_2();
# hitPoints = werewolf.getHitPoints();
# werewolf.takeMagicDamage(dmg);
# REQUIRE(werewolf.getHitPoints() == hitPoints - 35);
# }
# }
#
#
# TEST_CASE("Test for Wizard")
# {
#     Wizard
# wizard;
# Soldier
# target;
#
# SECTION("Wizard casts test")
# {
# int
# spellPower = wizard.getSpellPower();
# int
# newHP = target.getHitPoints() - spellPower;
#
# wizard.cast( & target);
# REQUIRE(target.getHitPoints() == newHP);
# REQUIRE(wizard.getMana() == 90);
# }
#
# SECTION("test for mana")
# {
# int
# hpTarget = target.getHitPoints();
#
# wizard.expendMana(100);
# REQUIRE(wizard.getMana() == 0);
# wizard.cast( & target);
# REQUIRE(target.getHitPoints() == hpTarget);
# wizard.addMana(150);
# REQUIRE(wizard.getMana() == 100);
#
# }
#
# SECTION("Change spell test")
# {
# wizard.cast( & target);
# REQUIRE(target.getHitPoints() == 170);
# wizard.changeSpell(3);
# wizard.cast( & target);
# REQUIRE(target.getHitPoints() == 185);
# wizard.changeSpell(2);
# wizard.cast( & target);
# REQUIRE(target.getHitPoints() == 130);
# wizard.changeSpell(4);
# wizard.cast( & target);
# REQUIRE(target.getHitPoints() == 155);
# }
#
# SECTION("Werewolf bite test")
# {
# Werewolf
# werewolf;
#
# werewolf.useAbilitiy_1( & wizard);
#
# REQUIRE(wizard.getMana() == 0);
#
# wizard.cast( & werewolf);
# REQUIRE(werewolf.getHitPoints() == 170);
#
# }
# }
#
# TEST_CASE("Test for Priest")
# {
#     Priest
# priest;
# Soldier
# target;
#
# SECTION("Priest cast test")
# {
# int
# newHp = target.getHitPoints();
#
# priest.changeSpell(1);
# priest.cast( & target);
# REQUIRE(target.getHitPoints() == newHp - priest.getSpellPower());
# priest.changeSpell(3);
# priest.cast( & target);
# REQUIRE(target.getHitPoints() == target.getHitPointsLimit());
# REQUIRE(priest.getMana() == 65);
# }
#
# SECTION("Physical attack test")
# {
# Necromancer
# necromancer;
# Vampire
# vampire;
# Werewolf
# werewolf;
#
# priest.attack( & necromancer);
# REQUIRE(necromancer.getHitPoints() == 86);
# priest.attack( & vampire);
# REQUIRE(vampire.getHitPoints() == 105);
#
# werewolf.useAbilitiy_1( & necromancer);
# priest.attack( & necromancer);
# REQUIRE(necromancer.getHitPoints() == 69);
# }
# }
#
# TEST_CASE("Test for Warlock")
# {
#     Warlock
# warlock;
#
# SECTION("Test for Demon")
# {
# warlock.cast();
# Soldier
# soldier;
# Vampire
# vampire;
# int
# amountOfDemeons = warlock.getAmountDemons();
#
# REQUIRE(warlock.getDemon(0)->getHitPointsLimit() == 80);
# REQUIRE(warlock.getDemon(0)->getDamage() == 30);
#
# warlock.getDemon(0)->attack( & soldier);
# REQUIRE(warlock.getDemon(0)->getHitPoints() == 58);
#
# vampire.useAbilitiy_1(warlock.getDemon(0));
# REQUIRE(warlock.getDemon(0)->getHitPointsLimit() == 80);
# REQUIRE(warlock.getDemon(0)->getDamage() == 30);
#
# try {
# vampire.attack(warlock.getDemon(0));
# vampire.attack(warlock.getDemon(0));
# }catch(...) {
# REQUIRE(warlock.getAmountDemons() == amountOfDemeons - 1);
# }
#
# }
#
# SECTION("Warlock cast test")
# {
# warlock.cast();
# REQUIRE(warlock.getMana() == 80);
#
# warlock.cast();
# REQUIRE(warlock.getMana() == 60);
#
# warlock.cast();
# warlock.cast();
# REQUIRE(warlock.getMana() == 20);
#
# warlock.getDemon(3)->attack( & warlock);
# REQUIRE(warlock.getHitPoints() == 100);
#
# warlock.cast();
# REQUIRE(warlock.getDemon(4) == 0);
# }
#
# SECTION("Dead of Warlock test")
# {
# warlock.cast();
# warlock.cast();
# warlock.cast();
#
# REQUIRE(warlock.getAmountDemons() == 3);
#
# try {
# warlock.takeDamage(130);
# warlock.takeDamage(1);
#
# } catch(...) {
# REQUIRE(warlock.getAmountDemons() == 0);
# }
# }
#
# SECTION("Vampire bite test")
# {
# Vampire
# vampire;
#
# vampire.useAbilitiy_1( & warlock);
# REQUIRE(warlock.getAmountDemons() == 0);
#
# warlock.cast();
# REQUIRE(warlock.getAmountDemons() == 0);
#
# vampire.attack( & warlock);
# REQUIRE(warlock.getHitPoints() == 83);
#
# }
# }
#
# TEST_CASE("Test for Necromancer")
# {
#     Necromancer
# necromancer;
# Necromancer
# necromancer2;
# Soldier
# soldier;
# Warlock
# warlock;
#
# SECTION("Attack test")
# {
# necromancer.attack( & soldier);
# necromancer2.attack( & soldier);
#
# necromancer.takeDamage(88);
# necromancer2.takeDamage(78);
# try{
# soldier.takeDamage(200);
# necromancer.attack( & soldier);
# }catch (...) {
# REQUIRE(necromancer.getHitPoints() == 76);
# REQUIRE(necromancer2.getHitPoints() == 86);
# }
#
# necromancer.attack( & necromancer2);
#
# try {
# necromancer2.takeDamage(50);
# necromancer.attack( & necromancer2);
# } catch (...) {
# REQUIRE(necromancer.getHitPoints() == 96);
# }
# }
#
# SECTION("Death of Necromancer test")
# {
# necromancer.attack( & soldier);
#
# try {
# necromancer.takeDamage(120);
# necromancer.takeDamage(100);
# }catch(...) {
# REQUIRE(necromancer.getHitPoints() == 0);
# }
#
# try {
# soldier.takeDamage(200);
# soldier.takeDamage(20);
# }catch(...) {
# REQUIRE(necromancer.getHitPoints() == 0);
# }
# }
#
# SECTION("Werewolf bite test")
# {
# Werewolf
# werewolf;
#
# necromancer.attack( & werewolf);
# werewolf.useAbilitiy_1( & necromancer);
# REQUIRE_FALSE(necromancer.isUndead());
#
# try {
# werewolf.takeDamage(150);
# necromancer.attack( & werewolf);
# }catch(...) {
# REQUIRE(necromancer.getHitPoints() == 100);
# }
# necromancer.attack( & soldier);
#
# try {
# soldier.takeDamage(160);
# necromancer.attack( & soldier);
# }catch (...) {
# REQUIRE(necromancer.getHitPoints() == 78);
# }
# }
#
# SECTION("Attack the Demon test")
# {
# warlock.cast();
# warlock.cast();
# warlock.cast();
# warlock.cast();
#
# necromancer.attack(warlock.getDemon(0));
#
# try {
# warlock.getDemon(0)->takeDamage(40);
# necromancer.attack(warlock.getDemon(0));
# }catch(...) {
# REQUIRE(necromancer.getHitPoints() == 120);
# }
#
# warlock.cast();
#
# necromancer.attack(warlock.getDemon(0));
# necromancer.attack(warlock.getDemon(1));
# necromancer.attack(warlock.getDemon(2));
# necromancer.attack(warlock.getDemon(3));
#
# necromancer.takeDamage(50);
# try {
# warlock.takeDamage(130);
# necromancer.attack( & warlock);
# }catch (...) {
# REQUIRE(necromancer.getHitPoints() == 114);
# }
# }
# }
