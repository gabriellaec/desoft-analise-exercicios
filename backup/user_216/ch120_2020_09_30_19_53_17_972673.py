#roleta
import random

grana = 100
while grana > 0:
    print(grana)
    apostado = int(input('Valor'))
    if apostado == 0:
        break
    elif apostado != 0:
        i = input('n/p')
        if i == 'n':
            x = random.randint(0,36)
            chute = int(input("Chute"))
            if chute == x:
                grana = grana + 35*apostado
            else:
                grana = grana - apostado
        else:
            x = random.randint(0,36)
            o = input('p/i')
            if o == 'p':
                if x %2 == 0:
                    grana = grana + apostado
                else:
                    grana = grana - apostado
            else:
                if x %2 != 0:
                    grana = grana + apostado
                else:
                    grana = grana - apostado