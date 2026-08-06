from library.books import find_by_author
from library.report import report_books
print(find_by_author('Агата Кристи'))
print(report_books()) #reports.py не запустилась напрямую потому что является дочерним модулем и лежит в пакете library. она работает корректно когда запускается в пакете вместе с другими модулями. 