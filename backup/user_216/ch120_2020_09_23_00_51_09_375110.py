import random
vi = 100
x = random.randint(0,36)
while vi > 0:
    print(vi)
    apostado = int(input('Quanto sera apostado'))
    y = input('n ou p')
    if y == 'n':
        c = int(input('Chute'))
        if c == x:
            vi = vi + apostado * 35
        else:
            vi = vi - apostado
    if y == 'p':
        d = input('p ou i')
        if d == 'p':
            if x %2 == 0:
                vi = vi + apostado
            else:
                vi = vi - apostado
        elif d =='i':
            if x % 2 != 0:
                vi = vi + adpostado
            else:
                vi = vi - apostado

