#from sys import exit
from random import randint

coins = 100
while coins > 0:
    print('Você possui {0} coins'.format(coins))
    valor = int(input('Qual valor vai apostar?: '))
    if valor == 0:
        coins = 0
    aposta = input('Você vai apostar em um número(n) ou em um par de números(p)?: ')
    if aposta == 'n':
        aposta_n = int(input('Aposte em um número de 1 a 36: '))
        resultado_n = randint(0, 36)
        print('O número sorteado foi: {0}'.format(resultado_n))
        if aposta_n == resultado_n:
            coins += valor*35
        else:
            coins -= valor
    if aposta == 'p':
        aposta_p = input('Par(p) ou ímpar(i)?: ')
        resultado_p = randint(0, 36)
        print('O número sorteado foi: {0}'.format(resultado_p))
        if resultado_p % 2 == 0:
            resultado_p = 'p'
        else:
            resultado_p = 'i'
        if aposta_p == resultado_p:
            coins += valor
        else:
            coins -= valor