def countvowels(text):
    counter = 0
    vowels = 'aiouey'
    for i in text:
        if i in vowels:
            counter += 1
    return counter
