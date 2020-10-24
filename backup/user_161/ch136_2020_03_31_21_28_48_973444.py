from random import randint

soma = randint(1, 6) + randint(1, 6) + randint(1, 6)

dinheiros = 10
fase_dicas = True
while fase_dicas:
    print('Você tem {0} dinehiros'.format(dinheiros))
    if dinheiros == 0 or input('Quer pedir uma dica? (não/sim) ') == 'não':
        fase_dicas = False
    else:
        dinheiros -= 1
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        n3 = int(input('Digite o terceiro número: '))
        if soma == n1 or soma == n2 or soma == n3:
            print('Está entre os 3')
        else:
            print('Não está entre os 3')
fase_chutes = True
while dinheiros > 0 and fase_chutes:
    print('Você tem {0} dinheiros'.format(dinheiros))
    if int(input('Digite seu chute: ')) == soma:
        dinheiros += dinheiros * 5
        fase_chutes = False
    else:
        dinheiros -= 1

if dinheiros > 0:
    print('Você ganhou o jogo com {0} dinheiros'.format(dinheiros))
else:
    print('Você perdeu')
