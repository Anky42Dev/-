import random
def get_random():
    secret = ''.join(random.sample('0123456789',3))
    return secret
def clues(secret, guess):
    clues = []
    if secret == guess:
        return 'You won'
    for i in range(len(secret)):
        if guess[i] in secret[i]:
            clues.append('Fermi')
        elif guess[i] in secret and guess[i] != secret[i]:
            clues.append('Pico')
        else:
            clues.append('Bagels')
    return ' '.join(clues)
def main():
    secret = get_random()
    guess = input()
    tries = 0
    while tries < 2:
        a = clues(secret,guess)
        print(a)
        tries += 1
        print(secret)
main()

    
