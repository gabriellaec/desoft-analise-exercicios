import random
D1 = random.randint(1,6)
D2 = random.randint(1,6)
D3 = random.randint(1,6)
SOMA = D1 + D2 + D3
dinheiros = 10

#FASE DE DICAS
print(dinheiros)
while dinheiros > 0:
    input('Jogador, chute um número: ')
    chute = int(input('Jogador, chute um número: '))
    dinheiros -= 1
    if chute == SOMA:
        print('Você ganhou o jogo com {0} dinheiros!.format(dinheiros)'
else:
    print('Você perdeu!')