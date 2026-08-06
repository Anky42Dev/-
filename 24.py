# def double_call(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#     return wrapper
# @double_call
# def greet(name):
#     print(f'Hello {name}')
# greet('Zaki')
class NegativeHealError(Exception):
    pass
def heal(hero, amount):
    if amount < 0:
        raise NegativeHealError('Восстановление не может быть отрицательным!')
    hero.hp += amount
try:
    heal('Zaki', -10)
except NegativeHealError as e:
    print(f'Ошибка: {e}')
finally:
    print('Проверка завершена')
    
    