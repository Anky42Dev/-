# 1. Супергерои (наследование, super().init(), полиморфизм)

# Создай базовый класс Hero с общими атрибутами: name, universe и power_level. От него унаследуй классы Spiderman, Batman и тд
# Во всех наследниках используй super().init(). Каждый герой должен по-своему реализовать метод use_power().
# Создай список героев и одним циклом вызови use_power() у каждого без использования if.
class Hero:
    def __init__(self,name,universe,powerlevel):
        self.name = name
        self.universe = universe
        self.powerlevel = powerlevel
    def use_power(self):
        print(f'{self.name} used his Superpower!')
class Spiderman(Hero):
    def __init__(self,name,universe,powerlevel):
        super().__init__(name,universe,powerlevel)    
    
    def use_power(self):
         print(f'{self.name} used Web shot!')
class Batman(Hero):
    def __init__(self,name,universe,powerlevel):
        super().__init__(name,universe,powerlevel)
    def use_power(self):
        print(f'{self.name} used  Echolocation!')
heroes = [
        Spiderman('Peter','Marvel',7),
        Batman('Bruce','Dc',9),
        Hero('Mark','Invincible',10)
    ]
for hero in heroes:
    hero.use_power()
# 2. Зоопарк (isinstance)

# Создай базовый класс Animal и наследников Lion, Wolf и Dragon. 
# Создай список животных и с помощью isinstance() определи тип каждого объекта, 
# выводя соответствующее действие (например, лев рычит, волк воет, дракон дышит огнем). 
# Затем посчитай, сколько животных каждого типа находится в списке.
class Animal:
    def __init__(self,type):
        self.type = type
class Lion(Animal):
    pass
class Wolf(Animal):
    pass
class Dragon(Animal):
    pass
animals = [Lion('Lion'),Wolf('Wolf'),Dragon('Dragon')]
for animal in animals:
    if isinstance(animal,Lion):
        print ('Rrr')
    elif isinstance(animal,Wolf):
        print('Auf')
    elif isinstance(animal,Animal):
        print('Wooooo')
