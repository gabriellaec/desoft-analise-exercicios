import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dados = dado1 + dado2 + dado3
din = 10
dicas = True
chutes = True
while dicas:
    print(din)
    if din == 0:
        print('Você perdeu!')
        dicas = False
        chutes = False
    else:
        dica = input('Quer uma dica por 1 dinheiro? (sim/não)')
        if dica == 'sim':
            n1 = int(input('Palpite 1: '))
            n2 = int(input('Palpite 2: '))
            n3 = int(input('Palpite 3: '))
            if n1 == dados or n2 == dados or n3 == dados:
                print('Está entre os 3')
            else:
                print('Não está entre os 3')
        else:
            dicas = False
while chutes:
    print(din)
    if din == 0:
        print('Você perdeu!')
        chutes = False
    else:
        c = int(input('Chute: '))
        if c == dados:
            din = 6 * din
            print('Você ganhou o jogo com {0} dinnheiros!'.format(din))
            chutes = False
        else:
            din -= 1