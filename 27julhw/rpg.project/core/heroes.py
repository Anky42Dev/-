from .items import Item
class 
class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if not self.name.is_alive():
            raise 

    def heal(self, amount, max_hp=100):
        self.hp = min(self.hp + amount, max_hp)

    def equip_item(self, item):
        item = Item(item.name, item.bonus_attack)
        print(f'{self.name} вооружился! Урон увеличен на {item.bonus_attack}')
        self.attack + item.bonus_attack
    
        