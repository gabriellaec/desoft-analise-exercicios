from random import randint

dinheiros = 100
aposta = input('Voce quer apostar? ')
print('Voce tem {0} dinheiros disponiveis'.format(dinheiros))
d1 = randint(1,6)
d2 = randint(1,6)
soma = d1 + d2            

while aposta != 'não':
    chute = int(input('Chute um numero: '))
    dinheiros -= 30
    if chute == soma:
        dinheiros += 50
        print('Parabens vc acertou')
        aposta = input('Voce quer apostar?')
    else:
        pergunta = input('Voce quer continuar tentando? ')
        if pergunta == 'desistir':
            aposta = input('Voce quer apostar? ')
            print('Voce tem {0} dinheiros'.format(dinheiros))
        else:
           chute2 = int(input('Chute um numero: '))
           dinheiros -= 20
           if chute2 == soma:
               dinheiros+=50
               print('Parabens vc acertou')
               aposta = input('Voce quer apostar? ')
               print('Voce tem {0} dinheiros'.format(dinheiros))
           else:
               dado = randint(d1,d2)
               print(dado)
               pergunta2 = print('Vai continuar tentando? ')
               print('Voce tem {0} dinheiros'.format(dinheiros))
               if pergunta2 == 'continuar':
                    chute3 = ('Chute um numero: ')
                    dinheiros -= 10
                    if chute3 == soma: