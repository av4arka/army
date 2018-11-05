class Abilitiy:


    def __init__(self, attacker):
        self._attacker = attacker

    def attack(self, enemy):
        self._attacker.ensure_is_alive()
        enemy.take_damage(self._attacker.damage)
        if enemy.hit_points > 0:
            self.counter_attack(enemy)

    def counter_attack(self, enemy):
        damage_enemy = enemy.damage / 2

        if enemy.title is 'Vampire':
            heal = self._attacker.hit_points_limit / 10

            enemy.add_hit_points(heal)

        self._attacker.take_damage(damage_enemy)
