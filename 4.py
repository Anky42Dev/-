# 1. Создай класс LogProcessor.
# 2. Напиши обычный метод __init__(self, raw_text), который сохраняет исходную строку лога.
# 3. Напиши @staticmethod с именем is_error(text). Он принимает строку и возвращает True,
# если в ней есть слово "ERROR", иначе False. (Нужен для быстрой фильтрации без создания объектов).
# 4. Напиши обычный метод format_log(self). Он проверяет текст текущего объекта через статический метод is_error. 
# Если это ошибка, возвращает "[CRITICAL] {текст}", иначе "[INFO] {текст}".
class Logprocessor:
    def __init__(self,raw_text):
        self.raw_text = raw_text

    @staticmethod
    def is_error(raw_text):
        if 'ERROR' in raw_text:
            return True
        else:
            return False
    def format_log(self):
        if self.is_error(self.raw_text):
            return f'[CRITICAL] {self.raw_text}'
        else:
            return f'[INFO] {self.raw_text}'
log1 = Logprocessor(" you haven't logged in")
print (log1.format_log())
log2 = Logprocessor("You've successfully logged in!")
print(log2.format_log())