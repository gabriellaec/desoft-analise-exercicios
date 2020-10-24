import random
d = 100
prog = True

while (prog and d > 0):
    print('{0}'.format(d))
    aposta = int(input('Quanto você deseja apostar: '))
    if aposta == 0:
        prog = False
    else:
        apostaX = input('A aposta é em um número(n) ou paridade(p)? ')
        if apostaX == 'n':
            n = int(input('Em qual número deseja apostar(1 - 36): '))
            r = random.randint(0,36)
            if n == r:
                d = d*35
            else:
                d = d-aposta
        elif apostaX == 'p':
            n = input('Escolha: par(p) ou ímpar(i): ')
            r = random.randint(0,36)
            if n == 'p':
                if r%2==0:
                    d = d+aposta
                else:
                    d = d-aposta
            elif n == 'i':
                if r%2==0:
                    d = d-aposta
                else:
                    d = d+aposta
            else:
                continue
        else:
            continue