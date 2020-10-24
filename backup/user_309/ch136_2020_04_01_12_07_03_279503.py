from random import randint

dinheiros = 10
d1 = randint(1,6)
d2 = randint(1,6)
d3 = randint(1,6)
soma = d1 + d2 + d3
print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
while dinheiros > 0:
    dica = input('Voce quer uma dica(s/n): ')
    if dica == 's':
        print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
        n1 = int(input('Fale um numero: '))
        n2 = int(input('Fale um numero: '))
        n3 = int(input('Fale um numero: '))
        if soma == n1 or soma == n2 or soma == n3:
            print('Está entre os 3')
        else:
            print('Não está entre os 3')
        dinheiros -= 1

    else:
        print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
        palpite = int(input('Qual seu palpite?(chute um número) '))
        if palpite == soma:
            dinheiros += dinheiros*5
        else:
            dinheiros -= 1
else:
    print('Você perdeu o jogo')
    
print('Voce ganhou o jogo com {0} dinheiros!'.format(dinheiros))