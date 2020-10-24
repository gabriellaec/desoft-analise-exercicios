import random
D1 = random.randint(1,6)
D2 = random.randint(1,6)
D3 = random.randint(1,6)
SOMA = D1 + D2 + D3
dinheiros = 10
N1= int(input('Jogador, chute um primeiro número: '))
N2= int(input('Jogador, chute um segundo número: '))
N3= int(input('Jogador, chute um terceiro número: '))
CHUTE= int(input('Jogador, chute um número: '))
#FASE DE DICAS
print(dinheiros)
if dinheiros = 0:
    print('Você perdeu!')
else:
    input('Você quer uma dica? s/n')
    QUER_DICA = input('Você quer uma dica? Sim/Não')
    while dinheiros > 0 and QUER_DICA = 'Sim':
        dinheiros -= 1
        input('Jogador, chute um primeiro número: ')
        input('Jogador, chute um segundo número: ')
        input('Jogador, chute um terceiro número: ')
        if SOMA = N1 or N2 or N3:
            print('Está entre os 3')
        else:
            print ('Não está entre os 3')
       
#FASE DE CHUTES
print(dinheiros)
if dinheiros = 0:
    print('Você perdeu!')
while dinheiros != 0:
    input('Jogador, chute um número: ')
    if CHUTE == SOMA:
        dinheiros = dinheiros*5
        print('Você ganhou o jogo com {0} dinheiros!.format(dinheiros)'
    else:
        dinheiros -= 1