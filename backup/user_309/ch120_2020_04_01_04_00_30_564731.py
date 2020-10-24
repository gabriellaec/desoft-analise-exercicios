import random
dinheiro = 100
while dinheiro > 0:
    print(dinheiro)
    aposta = int(input('Quanto vc quer apostar? '))
    if aposta != 0:
        n_ou_p = input('Voce quer apostar em n ou p? ')
        if n_ou_p == 'n'
            numero = int(input('Escolha um número entre 1 e 36: '))
            r1 = random.randint(0,36)
            if numero == r1:
                dinheiro += 35*aposta
            else:
                dinheiro -= aposta
        else:
            paridade = input('Escolha entre p ou i: ')
            r1 = random.randint(0,36)
            if paridade == 'p' and r1 % 2 == 0:
                dinheiro += aposta
            elif paridade == 'i' and r1 % 2 != 0:
                dinheiro += aposto
            else:
                dinheiro -= aposta
    else:
        dinheiro = 0