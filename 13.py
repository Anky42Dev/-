# ДЗ 1 — Переименуй и задокументируй (закрепление Блоков B–C)
# Дан плохо названный код. Переименуй все переменные и функцию так, чтобы имена были понятными, и добавь docstring.
def discount(price, quantity, discount_percent):
  """Функция находит цену товаров после скидки"""

  total_price = price * quantity
  return total_price - (total_price * discount_percent / 100)
print(discount(100,3,10))
print(discount.__doc__)
# ДЗ 2 — Найди и почини плохие комментарии 
# В коде ниже один комментарий — шум (пересказывает очевидное), а важного пояснения («почему именно 0.2») не хватает. 
# Убери лишний комментарий и добавь на его место комментарий, объясняющий смысл числа 0.2.
# def is_critical(self):
#     return self.hp < self.max_hp * 0.2 #если здоровье персонажа упало 20 процентов от макс хп то он в критическом положении


#ДЗ 3 - полный код ревью

# from .heroes import Hero

# def fight(hero1: Hero, hero2: Hero):
#     """В данной функции выполняется сражение между героями. """
#     while hero1.is_alive() and hero2.is_alive():

#         hero2.take_damage(hero1.attack)
#         print(f'{hero1.name} бьёт {hero2.name}, HP: {max(hero2.hp,0)}') # если hero.hp упало ниже 0 то будет выводиться 0 , не отрицательное число.
#         if not hero2.is_alive():
#             print(f'{hero2.name} побеждён!')
#             break

#         hero1.take_damage(hero2.attack)
#         print(f'{hero2.name} бьёт {hero1.name}, HP: {max(hero1.hp,0)}')
#         if not hero1.is_alive():
#             print(f'{hero1.name} побеждён!')

