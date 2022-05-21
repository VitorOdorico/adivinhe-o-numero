import random

def  guess(x):
    numero_aleatorio = random.randint(1, x)
    guess = 0
    while guess != numero_aleatorio :
        guess = int(input(f'Tente adivinhar um numero entre 1 a {x}'))
        if guess < numero_aleatorio:
            print('desculpe, tente novamente. Numero muito baixo')
        elif guess > numero_aleatorio:
            print('Desculpe, tente novamente, Numero muito alto')

    print('Ei, Parabens. Voce adivinhou o numero {numero_aleatorio} certo')
guess(10)      