
class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    def heal(self, amount, max_hp=100):
        self.hp = min(self.hp + amount, max_hp)
    
        