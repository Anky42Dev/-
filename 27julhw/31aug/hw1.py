# ДЗ 1 — Свой декоратор logger 
# Напиши декоратор logger,
#  который перед вызовом функции печатает её имя и переданные аргументы (используй func.name и args). 
#  Не забудь @wraps. Примени к любой функции с двумя аргументами и проверь через print(имя_функции.name), 
#  что имя не потерялось.
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'Func Name: {func.__name__}')
        print(f'Args Name: {args}')
        result = func(*args,**kwargs)
        return result
    return wrapper
name = input('What is your name? ')
date = 'Nice to hear you!'
@logger
def say_hello(name,date ):
    return f'Hello {name}! {date}'
print(say_hello(name,date))