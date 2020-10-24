import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dados = dado1 + dado2 + dado3
din = 10
dicas = True
chutes = True
while dicas:
    if din == 1:
        print('Sua carteira: 1 dinheiro')
    else:
        print('Sua carteira: ',din,' dinheiros')
    if din == 0:
        print('Você perdeu!')
        dicas = False
        chutes = False
    else:
        dica = 0
        while dica != 'sim' and dica != 'não':
            dica = input('Quer uma dica por 1 dinheiro? (sim/não)')
        if dica == 'sim':
            din -= 1
            n1 = 0
            n2 = 0
            n3 = 0
            while n1 < 3 or n1 > 18:
                n1 = int(input('Palpite 1: '))
            while n2 < 3 or n2 > 18:
                n2 = int(input('Palpite 2: '))
            while n3 < 3 or n3 > 18:
                n3 = int(input('Palpite 3: '))
            if n1 == dados or n2 == dados or n3 == dados:
                print('Está entre os 3')
            else:
                print('Não está entre os 3')
        else:
            dicas = False
while chutes:
    if din == 1:
        print('Sua carteira: 1 dinheiro')
    else:
        print('Sua carteira: ',din,' dinheiros')
    if din == 0:
        print('Você perdeu!')
        chutes = False
    else:
        c = 0
        while c < 3 or c > 18:
            c = int(input('Chute: '))
        if c == dados:
            din = 6 * din
            print('Você ganhou o jogo com {0} dinnheiros!'.format(din))
            chutes = False
        else:
            din -= 1