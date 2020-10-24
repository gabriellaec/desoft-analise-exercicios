import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
soma = dado1 + dado2 + dado3
dinheiro = 10

#FASE DE DICAS
while dinheiro > 0:
    print ('Você tem R${0}'.format(dinheiro))
    dica = input('Você quer uma dica?(sim/não) ')
    if dica == 'sim':
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        n3 = int(input('Terceiro número: '))
        if n1 == soma or n2 == soma or n3 == soma:
            print ('Está entre os 3')
        else:
            print ('Não está entre os 3')
    else:
        while dinheiro > 0:
            print ('Você tem R${0}'.format(dinheiro))
            chute = int(input('Chute um número: '))
            if chute == soma:
                dinheiro = dinheiro * 6
                break
            else:
                dinheiro = dinheiro - 1
        break
if dinheiro > 0:
    print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
else:
    print('Você perdeu!')