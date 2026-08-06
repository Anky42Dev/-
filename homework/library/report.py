from .stats import count_books 
def report_books():
    return f'Всего книг: {count_books()}'
