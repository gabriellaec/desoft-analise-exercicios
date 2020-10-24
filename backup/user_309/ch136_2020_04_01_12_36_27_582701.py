from random import randint

dinheiros = 10
d1 = randint(1,6)
d2 = randint(1,6)
d3 = randint(1,6)
soma = d1 + d2 + d3

dica = 'sim'
print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
if dinheiros > 0:
    while dica == 'sim':      
        dica = input('Voce quer uma dica(sim/não): ')

        if dica == 'sim':
            dinheiros -= 1
            print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
            n1 = int(input('Fale um numero: '))
            n2 = int(input('Fale um numero: '))
            n3 = int(input('Fale um numero: '))
            if soma == n1 or soma == n2 or soma == n3:
                print('Está entre os 3')
            else:
                print('Não está entre os 3')        

        
while dinheiros > 0:
    print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
    palpite = int(input('Qual seu palpite?(chute um número) '))
    if palpite == soma:
        dinheiros += dinheiros*5
        print('Voce ganhou o jogo com {0} dinheiros!'.format(dinheiros))
        break

    else:
        dinheiros -= 1
        
if dinheiros == 0:
    print('Você perdeu o jogo')
    