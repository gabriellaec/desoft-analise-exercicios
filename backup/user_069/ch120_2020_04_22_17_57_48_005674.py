import random 
d = 100
jogando = True 
while jogando:
    print('Você tem {0}'.format(d))
    if d == 0:
        break
    a = int(input("Aposte um valor: "))
    if a == 0 or a > d:
        break
    else:
        b = input("A aposta é um número ou paridade? ")
        e = random.randint(1, 36)
        if b == 'n':
            c = int(input("chute um número de 1 a 36: "))
            if c == e:
                d += 35*a
                print('Você tem {0}'.format(d))
            else:
                d -= a
                print('Você tem {0}'.format(d))
        elif b == 'p':
            f = input("Escolha entre par (p) ou impar (i): ")
            if f == 'p':
                if e%2 == 0:
                    d += a
                    print('Você tem {0}'.format(d))
                else:
                    d -= a
                    print('Você tem {0}'.format(d))
            if f == 'i':
                if e%2 == 0:
                    d -= a
                    print('Você tem {0}'.format(d))
                else:
                    d += a
                    print('Você tem {0}'.format(d))
      