# Задача 2: Валютный Конвертер (Classmethod)

#  Создай класс для конвертации валют с единым глобальным курсом.

# 1. Создай класс Converter. У него должен быть атрибут класса usd_rate = 85.0 (курс доллара).
# 2. Напиши обычный метод __init__(self, amount_som), который сохраняет сумму в сомах.
# 3. Напиши обычный метод to_usd(self). Он делит сумму в сомах на текущий usd_rate класса и возвращает результат.
# 4. Напиши @classmethod с именем update_rate(cls, new_rate). Он должен обновлять значение usd_rate сразу для всего класса.
class Converter:
    usd_rate = 85.0
    def __init__(self,amount_som):
        self.amount_som = amount_som
    def to_usd(self):
        return self.amount_som / Converter.usd_rate
    @classmethod
    def update_rate(cls,new_rate):
        cls.usd_rate = new_rate
        return cls.usd_rate
        
money1 = Converter(8500)
print(money1.to_usd())
print(Converter.update_rate(87.0))