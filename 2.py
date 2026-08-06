# 2. BankAccount (семейный бюджет)
# BankAccount(owner, balance)eqвить: __eq__ — равны если совпаltwner, __lt__ — меньше по balance (дadded), __add__ — слияние в "Семейный" счёт (сумма балансов), но если у одного balance < 0 — raise ValueError, __len__ — количество полных тысяч на счету.
# Проверить: 5 счетов, sorted() по балансу, слить два (один с долгом) через try/except.
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'{self.owner} {self.balance}'
    def __eq__(self,other):
        if self.owner == other.owner:
            return 'один владелец'
        else:
            return 'Разные владельцы'
    def __lt__(self,other):
         return self.balance<other.balance
    def __add__(self,other):
        family = self.balance + other.balance
        if other.balance < 0 or self.balance < 0:
            raise ValueError
        else:
            return family
owner1 = BankAccount('Patrick Bateman',7000)
owner2 = BankAccount('Patrick Bateman',3000)
owner3 = BankAccount('Paul Allen',10000)
owner4 = BankAccount('Tyler Derden',3000)
owner5 = BankAccount('Jesse Pinkman',-700)
owners =[owner1,owner2,owner3,owner4,owner5]
for i in sorted(owners):
    print(i) # Вывод обьектов
try:
    print(owner1+owner4)
except ValueError:
    print('Нельзя обьединить! Есть долг')
print(owner1 == owner3)