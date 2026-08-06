# Напиши функцию game_card(title, **info), которая возвращает строку вида "Valorant, Genre: FPS, Release year: 2020". 
# Требования: поля выводятся в алфавитном порядке ключей;
# если в ключе есть _ (нижнее подчёркивание) — замени на пробел и сделай первую букву заглавной (release_year → Release year).
def game_card(title,**info):
    result = title
    for key in sorted(info):
        new_key = key.replace('_',' ').capitalize()
        result += f', {new_key} : {info[key]}'
    return result
print(game_card("Valorant", genre="FPS", release_year=2020))
print(game_card("Minecraft"))