import random
roleta=random.randint(0, 36)
fichas=100
while not fichas == 0:
    print('Você tem {0} fichas'.format(fichas))
    aposta=int(input('Quanto você vai apostar:'))
    resposta=input('Como você vai aposta:')
    if aposta == '0':
        break
    elif resposta=='n':
        x=int(input('Em qual número você vai apostar:'))
        if roleta == x:
            fichas=fichas+aposta*35
        else:
            fichas=fichas-aposta
    elif resposta=='p':
        x=input('Par ou Ímpar:')
        if x=='p':
            if roleta%2==0:
                fichas=fichas+aposta*2
            else:
                fichas=fichas-aposta
        elif resposta=='i':
            if roleta%2!=0:
                fichas=fichas+aposta*2
            else:
                fichas=fichas-aposta
        else:
            print('Resposta inválida')
    else:
        print('Resposta inválida')
    roleta=random.randint(0, 36)