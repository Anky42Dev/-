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
        return self.power>0
card1 = Card('The Star',7)
card2 = Card('The Magician',5)
card3 = Card('The Archon',6)
card4 = Card('Dead', 0)
cards =  [card1,card2,card3,card4]
n = max(cards)
print(n)
print(card2>card1)
print(card1 +card2)
if card4:
    print('Карта жива')
else:
    print('Карта мертва')
# 2. BankAccount (семейный бюджет)
# BankAccount(owner, balance)eqвить: __eq__ — равны если совпаltwner, __lt__ — меньше по balance (дadded), __add__ — слияние в "Семейный" счёт (сумма балансов), но если у одного balance < 0 — raise ValueError, __len__ — количество полных тысяч на счету.
# Проверить: 5 счетов, sorted() по балансу, слить два (один с долгом) через try/except.

# 3. Timer (обратный отсчёт)
# Timer(label, seconds). Добавить: __str__ → ltние: 90 сек", __lt__ —sub по seconds, __sub__ — вычесть секунды из таймера, возвращает новый Tiboolменьше 0!), __bool__ — True если seconds > 0.
# Проверить: создать 3 таймера, отсортировать, у одного вычесть время дважды, чтобы дошёл до 0, проверить bool().