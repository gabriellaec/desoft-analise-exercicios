'''Essa fução
'''
import random
dinheiros = 10
dado1 = random.randint(1,10)
dado2 = random.randint(1,10)
soma_dados = dado1 + dado2
numero = int(input('Escolha um número entre 2 e 20: '))
numero2 = int(input('Escolha um numero maior ou igual ao anterior: '))
if soma_dados < numero:
    print('Soma menor')
elif soma_dados > numero2:
    print('Soma maior')
else:
    print('Soma no meio') 
print(dinheiros)
chutes = int(input('Quantos chutes deseja compra? '))
saldo = dinheiros - chutes
while dinheiros > 0:    
    numero = int(input('Escolha um número entre 2 e 20: '))
    numero2 = int(input('Escolha um numero maior ou igual ao anterior: '))
    if soma_dados < numero:
        print('Soma menor')
    elif soma_dados > numero2:
        print('Soma maior')
    else:
        print('Soma no meio')
    if soma_dados == numero or soma_dados == numero2:
        dinheiros += saldo *5
        print('Você terminou o jogo com {0} dinheiros'.format(dinheiros))
        break
    elif chutes == 0:
        break
print('Você terminou o jogo com {0} dinheiros'.format(dinheiros))