#Exercício 4

import random
dinheiro = 100
valor = 1
while dinheiros != 0 and valor != 0:
    print('Você tem {0} dinheiros'.format(dinheiro))
    valor = int(input('Digite um valor'))
    if valor != 0:
        aposta = input('Sua aposta é um numero ou uma paridade? (Digite n ou p)' )
        roleta = random.randint(0,36)
        if aposta == 'n':
            numero = int(input('Digite um número de 0 a 36.')
            if numero == roleta:
                dinheiro = dinheiro + aposta * 35
                print(dinheiro)
            else:
                dinheiro = dinheiro - aposta
                print(dinheiro)
        elif aposta == 'p':
            par_ou_impar = input('Você escolhe par ou impar? (digite par ou impar)')
            if roleta %2==0:
                if par_ou_impar == 'par':
                    dinheiro = dinheiro + valor
                    print(dinheiro)
                elif par_ou_impar == 'impar':
                    dinheiro = dinheiro - valor
                    print(dinheiro)

            elif roleta % 2 != 0:
                if par_ou_impar == 'impar':
                    dinheiro = dinheiro + valor
                    print(dinheiro)
                else:
                    dinheiro = dinheiro - valor
                    print(dinheiro)
                   
print('Game over')