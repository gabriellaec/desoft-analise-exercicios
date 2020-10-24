import random
vi = 100

while vi > 0:
    print(vi)
    apostado = int(input("Apostar"))
    if apostado == 0:
        break
    b = input('Numero ou Paridade?')
    if b == 'n':
        valor = int(input("Numero chutado"))
    if b == 'p':
        c = input('Par ou impar')
    x = random.randint(0,36)
    if b == 'n':
        if valor == x:
            vi = vi + 35 * apostado
        else:
            vi = vi - apostado
    elif b == 'p':
        if c == 'p' and x %2 == 0:
            vi = vi + apostado
        elif c == 'i' and x %2 != 0:
            vi = vi + apostado
        else:
            vi = vi - apostado