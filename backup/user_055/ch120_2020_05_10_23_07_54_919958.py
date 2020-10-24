from time import sleep
from sys import exit
from random import randint

coins = 100
while coins > 0:
    #sleep(1)
    print('Você possui {0} coins'.format(coins))
    #sleep(1)
    valor = int(input('Qual valor vai apostar?: '))
    if valor == 0:
        exit()
    #sleep(1)
    aposta = input('Você vai apostar em um número(n) ou em um par de números(p)?: ')
    #sleep(1)
    if aposta == 'n':
    #    sleep(1)
        aposta_n = int(input('Aposte em um número de 1 a 36: '))
    #   sleep(1)
        resultado_n = randint(1, 36)
        print('O número sorteado foi: {0}'.format(resultado_n))
        if aposta_n == resultado_n:
            coins += valor*35
        else:
            coins -= valor
     #   sleep(1)
    if aposta == 'p':
        aposta_p = input('Par(p) ou ímpar(i)?: ')
     #  sleep(1)
        resultado_p = randint(1, 36)
        print('O número sorteado foi: {0}'.format(resultado_p))
        if resultado_p % 2 == 0:
            resultado_p = 'p'
        else:
            resultado_p = 'i'
        if aposta_p == resultado_p:
            coins += valor
        else:
            coins -= valor
     #   sleep(1)