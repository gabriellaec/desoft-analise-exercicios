import random
d = 100
prog = True

while (prog):
    r = random.randint(1,36)
    print('Você tem ${0}'.format(d))
    aposta = int(input('Quanto você deseja apostar: '))
    if aposta == 0:
        prog = False
    elif d <= 0:
        prog = False
    elif aposta > d:
        print('Você não pode apostar mais dinheiro do que tem!')
        continue
    else:
        apostaX = input('A aposta é em um número(n) ou paridade(p)? ')
        if apostaX == 'n':
            n = int(input('Em qual número deseja apostar(1 - 36): '))
            if n == r:
                d = d*35
            else:
                d = d-aposta
        elif apostaX == 'p':
            n = input('Escolha: par(p) ou ímpar(i): ')
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
                print('Digite "p" para par ou "i" para ímpar APENAS')
                continue
        else:
            print('Digite "n" para apostar em um número ou "p" para apostar em par ou ímpar ')
            continue