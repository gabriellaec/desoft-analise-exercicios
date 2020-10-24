import math
import random

dinheiro=100

while dinheiro>0:
    print('Seu dinheiro é: {0}'.format(dinheiro))
    aposta=int(input('Aposte um valor [zero para parar]: '))
    if aposta==0:
        break
    pergunta=input('A aposta é em um número ou paridade? ')
    if pergunta=='n':
        rn=random.randint(0,36)
        cn=int(input('Digite um número de 1 a 36: '))
        if cn==rn:
            dinheiro+=aposta*35
        else:
            dinheiro-=aposta
    elif pergunta=='p':
        rp=random.randint(0,36)
        if rp%2==0:
            rp='p'
        else:
            rp='i'
        cp=input('Digite "p" [para par] ou "i" [para ímpar]: ')
        if cp==rp:
            dinheiro+=aposta
        else:
            dinheiro-=aposta
            
print('O jogo acabou!')