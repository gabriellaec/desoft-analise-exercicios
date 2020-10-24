dinheiro = 10
print('Você possui {0} dinheiros'.format(dinheiro))
i = True
if dinheiro = 0:
    i = False
else:
    i = True

while i:
    quer_dica = input('Você quer uma dica?(sim/não) ')
    if quer_dica == 'sim':
        dinheiro -= 1
        print('Você possui {0} dinheiros'.format(dinheiro))
        digite_1 = int(input('Digite um número: '))
        digite_2 = int(input('Digite um número: '))
        digite_3 = int(input('Digite um número: '))
        if dado1 = digite_1 or dado1 = digite_2 or dado1 = digite_3 or dado2 = digite_1 or dado2 = digite_2 or dado2 = digite_3 or dado3 = digite_1 or dado3 = digite_2 or dado3 = digite_3: 
            print("Está entre os 3")
        else:
            print("Não está entre os 3")        
    elif quer_dica == 'não':
        print('Você possui {0} dinheiros'.format(dinheiro))
        digite_chute = input('Digite seu chute: ')
        if soma == digite_chute:
            dinheiro = dinheiro + dinheiro*5
            print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
        else:
            dinheiro -= 1
            print('Não acertou')
else: 
        print('Você perdeu!')
            