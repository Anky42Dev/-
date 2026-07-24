from core.heroes import Hero
from core.battle import fight
from core.items import Item

arthur = Hero('Артур', hp=50, attack=8)
villain = Hero('Тёмный рыцарь', hp=40, attack=10)
commander = Hero('Тресдин',hp = 70, attack = 9)

sword = Item('Frostmourne', bonus_attack = 4)
halberd = Item('Heaven', bonus_attack = 2)

arthur.heal(1)  # используем метод из heroes.py перед боем
fight(arthur, villain)
arthur.heal(10)
arthur.equip_item(sword)
commander.equip_item(halberd)
fight(arthur,commander)
