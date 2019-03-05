# Army
### The task:
Basic unit types:
- Unit: warrior specializing in physical damage
- SpellCaster: warrior specializing in magical damage

It is logical that all units that inflict magical damage can also inflict physical  
damage. The physical damage that SpellCaster inflicts should be small, just as  
SpellCaster has a smaller number of health points compared to Unit.

Physical damage units:  
- Soldier: unit without any special abilities  
- Rogue: units don't counterattack him   
- Berserker: magic does not affect berserkers  
- Vampire: when attacking / counterattacking consumes part of the life force of the enemy  
- Werewolf: able to turn into a wolf (in the wolf state has a higher indicator of vitality  
and attack, but receives more damage from magic)

Magic damage units:  
- Wizard: attacks with combat spells (healing spells have only half the power)  
- Healer: owns healing spells (combat spells have only half the power)  
- Priest: owns healing spells (combat spells have only half the power), deals x2 damage  
to the undead (Vampire, Necromancer)  
- Warlock: summons demons (Demon class slightly expands Soldier class)  
- Necromancer: monitors all those who attacked, in the event of the death of the attacked  
unit, receives a part of its vitality

Interfaces:  
- Observer: use for Necromancer  
- Observable: use for all others  

Additional features:  
- A vampire can make another unit a vampire (except Werewolf)  
- A werewolf can make another unit a werewolf (except Vampire)  

### For example:
##### Units attack:
```python
    berserker = Berserker()
    soldier = Soldier()
    roque = Roque()
    vampire = Vampire()
    werewolf = Werewolf()

    # soldier hp = 200, roque hp = 150
    soldier.attack(roque)
    # soldier hp = 180, roque hp = 105
    roque.attack(soldier)
    # roque hp = 105, units don't counterattack him
    soldier.attack(vampire)
    # vampire hp = 105, vampire to be treated
    berserker.take_magic_damage(100)
    #berserker is immune to magic
    werewolf.use_abilitiy_two()
    #werewolf transformed in wolf
    werewolf.use_abilitiy_one(soldier)
    #werewolf turned the soldier into werewolf, and soldier has the same abilitiy and state 
```
#### Spellcasters abilities:
```python
    wizard = Wizard()
    healer = Healer()
    priest = Priest()
    warlock = Warlock()
    necromancer = Necromancer()
    soldier = Soldier()
    vampire = Vampire()

    #soldier hp = 200
    wizard.use_abilitiy_one(soldier)
    #soldier hp = 170, wizard use default spell - lightning
    healer.use_abilitiy_one(soldier)
    #soldier hp = 200, healer use default spell heal
    healer.change_spell(1)
    #healer changed spell, 1 = lightning
    healer.use_abilitiy_one(soldier)
    #soldier hp = 185
    priest.attack(vampire)
    #priest deals x2 damage to the undead
    warlock.use_abilitiy_two()
    #warlock created the demon
    warlock[0].attack(soldier)
    #the demon attacked the soldier
    necromancer.attack(soldier)
    #The necromancer attacked the soldier, after the death of 
    # the soldier the necromancer will receive some of his vitality
```

### Installation instructions
- 1)Clone this repository 
- 2)Import modul my_army in folder my_army
- 3)Use this code
