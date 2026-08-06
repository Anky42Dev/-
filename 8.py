# Прямоугольник (геометрия)
# Задание
# Напиши класс Rectangle. Атрибуты: width и height. Методы: area() — ВОЗВРАЩАЕТ площадь (не печатает!); 
# perimeter() — возвращает периметр; is_square() — 
# возвращает True, если это квадрат. Создай пару прямоугольников и напечатай их площади через переменную.4
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) *2
    def is_square(self):
        return self.width == self.height
rect1= Rectangle(2,4)
rect2= Rectangle(2,2)
print(rect2.is_square())
print(rect1.perimeter())

# Плейлист (список внутри объекта)
# Задание
# Напиши класс Playlist. Атрибуты: name (название плейлиста) и
# songs (список песен, по умолчанию пустой). Методы: add(song) — 
# Добавить песню в список; remove(song) — убрать песню, если она есть; show() — 
# напечатать все песни по порядку с номерами; count() — вернуть количество песен.
#  Создай плейлист, добавь 3–4 песни, одну убери, покажи результат.
class Playlist:
    song = []
    count = 0
    def __init__(self,name):
        self.name = name  
        Playlist.count += 1
    def add(self):
        Playlist.song.append(self.name)
        return Playlist.song
    def removed(self):
        Playlist.song.remove(self.name)
        Playlist.count -= 1
        return Playlist.song
    def show():
        print ('Here is songs from your Playlist:')
        for number,song in enumerate(Playlist.song ,start = 1):
            print(f'{number}. {song}') 
    def counter():
        return f'You have {Playlist.count} songs'
        
            
song1 = Playlist('505')
song2 = Playlist('Animals')
song3 = Playlist('Loba')
song2.add()
song1.add()
song3.add()
song3.removed()
# song1.removed()
Playlist.show()
print(Playlist.counter())

        

        

