# Задача 1 — форматирование цен для интернет-магазина
# На бэкенде интернет-магазина цены хранятся как обычные числа, а на сайте их нужно показывать 
# с валютным символом. Напиши функцию create_price_formatter(currency_symbol), 
# которая возвращает вложенную функцию format_price(amount) — 
# она форматирует число до двух знаков после запятой и добавляет символ валюты
def create_price_formatter(currency_symbol):  
    def format_price(amount):
        return f'{amount:.2f} {currency_symbol}'
    return format_price
format_usd = create_price_formatter("$")
format_eur = create_price_formatter("€")

print(format_usd(19.9))
print(format_eur(45))
# Задача 2 — валидатор формы регистрации
# В форме регистрации нужно проверять email и возраст пользователя. 
# Напиши функцию create_registration_validator(),
# внутри которой объявлены ДВЕ вложенные функции: 
# is_valid_email(email) — проверяет, что в строке есть символ @, и is_valid_age(age) — проверяет, 
# что возраст от 13 до 120. Основная функция возвращает обе
def create_registration_validator():
    def is_valid_email(email):
        return '@' in email
    def is_valid_age(age):
        return 13<=age<120
    return is_valid_email, is_valid_age

is_valid_email, is_valid_age = create_registration_validator()
print(is_valid_email("kira@mail.com"))
print(is_valid_email("kira-mail.com"))
print(is_valid_age(16))
print(is_valid_age(5))
# Задача 3 — счётчик обращений к API (общее состояние)
# На сервере нужно считать, сколько раз к определённому эндпоинту API обратились клиенты — 
# для мониторинга нагрузки. Напиши функцию create_request_logger() с переменной count = 0 
# внутри и двумя вложенными функциями: log_request() — увеличивает счётчик на 1, и get_count() — 
# просто возвращает текущее значение, ничего не меняя.
def create_request_logger():
    count = 0
    def log_request():
        nonlocal count
        count += 1
    def get_count():
        return count
    return log_request,get_count
log_request, get_count = create_request_logger()
log_request()
log_request()
log_request()
print(get_count())
# Задача 4 — генератор номеров заказов
# В системе интернет-магазина каждому новому заказу нужен уникальный номер, который увеличивается на 1 с 
# каждым новым заказом (например, ORD-1001, ORD-1002...). Напиши функцию create_order_id_generator(start), 
# которая возвращает вложенную функцию next_id() — 
# она увеличивает внутренний счётчик и возвращает строку вида "ORD-1001".
def create_order_id_generator(start):
    def next_id():
        nonlocal start
        start +=1
        return f'ORD-{start}'
    
    return next_id

next_id = create_order_id_generator(1000)

print(next_id())
print(next_id())
print(next_id())