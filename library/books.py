books = {'Лолита':'Набоков',
         '451 по Фаренгейту':'Рэй Брэдбери',
         '10 негритят':'Агата Кристи'}
def find_by_author(author):
    for title,book_author in books.items():
        if author == book_author:
            return title
    return 'Книги этого автора нет'
