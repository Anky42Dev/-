# ДЗ 2 — Своё исключение InvalidNameError 
# В классе Hero добавь проверку в init: если name — пустая строка, вызвать своё исключение InvalidNameError с понятным текстом. 
# Оберни создание героя с пустым именем в try/except и убедись, что герой с нормальным именем создаётся без ошибок.
class Hero:
    def __init__(self,name):
        self.name = name 
        if not self.name:
            raise InvalidNameError('Имя не может быть пустым')
class InvalidNameError(Exception):
    def find_error():
        pass
try:
    a = Hero('')
except  InvalidNameError as e:
    print(e)
finally:
    print('Проверка завершена')
