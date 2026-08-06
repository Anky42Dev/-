books = [{'title':'Лолита','author':'Набоков'},
         {'title':'451 по Фаренгейту','author':'Рэй Брэдбери'},
         {'title':'10 негритят','author':'Агата Кристи'}]
def find_by_author(author):
        result = []
        for book in books:
            if book['author'] == author:
                result.append(book['title'])
        return ','.join(result)

