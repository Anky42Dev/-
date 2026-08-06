# def is_digit(string):
#     """Проверяет является ли текст числом"""
#     # is_number = string.isdigit()
#     return string.isdigit()
# # print(is_digit('apple'))
# # print(is_digit.__doc__)
# help(is_digit)
# heroes.py
class Hero:
    """Персонаж у которого есть имя , здоровье, урон."""
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        """Проверяет жив ли наш Герой"""
        return self.hp > 0

    def is_attacked(self, amount):
        """Герой получает урон """
        self.hp -= amount

    def get_healed(self, amount, max_hp=100):
        """ Восстанавливает здоровье героя"""
        self.hp = min(self.hp + amount, max_hp)
