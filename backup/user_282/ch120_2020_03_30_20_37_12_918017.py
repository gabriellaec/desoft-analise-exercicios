import random

dinheiro = 100
while dinheiro>0:
    print('voce tem {0} reais'.format(dinheiro))
    aposta = int(input('quanto voce aposta? '))
    número_ou_paridade = input('é n ou p? ')
    sorteio = random.randint(1, 36)
    if aposta == 0:
        break
    elif número_ou_paridade == 'n':
        numero = int(input('digite um numero de 1 a 36: '))
        if numero == sorteio:
            dinheiro += 35*aposta
        else:
            dinheiro -= aposta
    elif número_ou_paridade == 'p':
        par_ou_impar = input('pár ou impár? ')
        if par_ou_impar == 'pár' and sorteio%2 == 0:
            dinheiro += aposta
        elif par_ou_impar == 'impár' and sorteio%2 != 0:
            dinheiro += aposta
        else:
            dinheiro -= aposta