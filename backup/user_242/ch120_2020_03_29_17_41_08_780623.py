#Exercício 4

import random
dinheiros = 100
valor = 1
while dinheiros != 0 and valor != 0:
    print('Você tem {0} dinheiros'.format(dinheiros))
    valor = int(input('Digite um valor'))
    if valor != 0:
        aposta = input('Sua aposta é um numero ou uma paridade? (Digite n ou p)' )
        sorteio = random.randint(0,36)
        if aposta == 'n':
            numero = int(input('Digite um número de 0 a 36.')
            if numero == sorteio:
                dinheiros = dinheiros + aposta * 35
                print(dinheiro)
            else:
                dinheiros = dinheiros - aposta
                print(dinheiros)
        elif aposta == 'p':
            par_ou_impar = input('Você escolhe par ou impar? (digite par ou impar)')
            if sorteio %2==0:
                if par_ou_impar == 'par:
                    dinheiros = dinheiros + valor
                    print(dinheiros)
                elif paa_ou_impar == 'impar':
                    dinheiros = dinheiros - valor
                    print(dinheiros)
                    if dinheiros == aposta:
                        dinheiros == 0 

            elif sorteio % 2 != 0:
                if par_ou_impar == 'impar':
                    dinheiros = dinheiros + valor
                    print(dinheiros)
                else:
                    dinheiros = dinheiros - valor
                    print(dinheiros)
                   
print('Game over')