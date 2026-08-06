# 1. Card (карточная битва)
# Card(name, power). Добавить: __str__, __gt__ (не __lt__!) — сильнеaddwer,
#  __add__ — комбо-карта (имя через "+", сила = сумма bool%),
#   __bool__ — жива если power>0.
# Проверить: 4 карты, найти сильнейшую через max(),
# объединить две любые.
class Card:
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def __str__(self):
        return f'Name: {self.name}, Power level: {self.power}'
    def __gt__(self,other):
        return self.power > other.power
    def __add__(self,other):
        newcard = self.power + other.power + (self.power+other.power)//2
        return f'Комбо-карта! Сила стала {newcard}'
    def __bool__(self):
        return self.name != ''
card1 = Card('The Star',7)
card2 = Card('The Magician',5)
card3 = Card('The Archon',6)
card4 = Card('Dead', -10)
cards =  [card1,card2,card3,card4]
n = max(cards)
print(n) #вывод сильнейшего
print(card2>card1) 
print(card1 +card2) #Обьединение карт
if card4:
    print('Карта жива')
else:
    print('Карта мертва')