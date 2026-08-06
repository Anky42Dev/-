# 3. Timer (обратный отсчёт)
# Timer(label, seconds). Добавить: __str__ → ltние: 90 сек", __lt__ —sub по seconds,
# __sub__ — вычесть секунды из таймера, возвращает новый Tiboolменьше 0!), __bool__ — True если seconds > 0.
# Проверить: создать 3 таймера, отсортировать, у одного вычесть время дважды, чтобы дошёл до 0, проверить bool().
class Timer:
    def __init__(self,label,seconds):
        self.label = label
        self.seconds = seconds
    def __str__(self):
        return f'{self.label}-{self.seconds} секунд'
    def __lt__(self,other):
        return self.seconds <other.seconds
    def __sub__(self,other):
        new = self.seconds - other.seconds
        if new < 0:
            new =  0 
        return Timer(self.label, new)
    def __bool__(self):
        return self.seconds > 0
tea = Timer('Tea',120)
prep = Timer('Preparation',90)
jog = Timer('Jog',60)
times = [tea,prep,jog]
for i in sorted(times):
    print(i)
a = jog - tea
print(a)
print(bool(a))

