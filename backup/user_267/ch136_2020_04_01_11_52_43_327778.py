import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
soma = dado1 + dado2 + dado3
dinheiro = 10
print('Você possui 10 dinheiros')
while dinheiro > 0:
    quer_dica = input('Você quer uma dica?(sim/não) ')
    if quer_dica == 'sim':
        dinheiro -= 1
        digite_1 = int(input('Digite um número: '))
        digite_2 = int(input('Digite um número: '))
        digite_3 = int(input('Digite um número: '))
        for (dado1 or dado2  or dado3) in [digite_1,digite_2,digite_3]:
            print("Está entre os 3") 
        else:
            print("Não está entre os 3")
    else:
        print('Você possui {0} dinheiros'.format(dinheiro))
        digite_chute = input('Digite seu chute: ')
        if soma == digite_chute:
            dinheiro += dinheiro*5
            print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
        else:
            dinheiro -= 1
            print('Não acertou')
else: 
    print('Você perdeu!'
            
        
