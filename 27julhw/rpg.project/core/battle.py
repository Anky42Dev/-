 # ДЗ 3 — Полная связка 
# Возьми свой battle.py из проекта rpg_project и добавь: 1 декоратор retry_on_error(func),
# который, если внутри украшенной функции возникло любое исключение, ловит его, печатает 
# «Повтор после ошибки: {e}» и вызывает функцию ещё раз; 2 своё исключение HeroDefeatedError — вызывается, 
# если кто-то пытается нанести урон герою, который уже не is_alive(); 
# 3 try/except/finally вокруг всего боя. Подсказка: чтобы поймать ошибку изнутри декоратора, нужно обернуть в
# try/except именно вызов func(*args, **kwargs) внутри wrapper. -->
from .heroes import Hero
from functools import wraps
class HeroDefeatedError("Герой уже мертв!"):
    pass

def retry_on_error(func):
    wraps(func)
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except HeroDefeatedError as e:     
            print(f'Повтор после ошибки: {e}')
        finally:
            print('Бой окончен')
        result = func
        return result
    return  wrapper
        
@retry_on_error
def fight(hero1: Hero, hero2: Hero):
    while hero1.is_alive() and hero2.is_alive():
        hero2.take_damage(hero1.attack)
        print(f'{hero1.name} бьёт {hero2.name}, HP: {max(hero2.hp,0)}')
        if not hero2.is_alive():
            print(f'{hero2.name} побеждён!')
            break

        hero1.take_damage(hero2.attack)
        print(f'{hero2.name} бьёт {hero1.name}, HP: {max(hero1.hp, 0)}')
        if not hero1.is_alive():
            print(f'{hero1.name} побеждён!')

