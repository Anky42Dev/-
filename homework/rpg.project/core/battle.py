from .heroes import Hero


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
