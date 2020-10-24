import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
soma = (dado1 + dado2 + dado3)
dinheiro = 10
print('Você possui {0} dinheiros'.format(dinheiro))
    while dinheiro != 0:
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