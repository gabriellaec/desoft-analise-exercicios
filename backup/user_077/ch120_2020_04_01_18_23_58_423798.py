from random import randint
print('100$')
a=100
b=True
while b:
    if a<=0:
        print('Fim de Jogo')
        b=False
    else:
        c=int(input('aposte um valor'))
        if c<=0 or c>a:
            b=False
        else:
            d=input('número ou paridade?')
            if d=='n':
                e=int(input(' digite um número de 1 a 36')
                f=randint(1,36)
                if e==f:
                    a=a+(35*c)
                    print ('Ganhou!')
                    print('Você agora tem ${0}'.format(a))
                    b=True
                else:
                    print('Perdeu!')
                    a=a-c
                    print('Você agora tem ${0}'.format(a))
                    b=True
            if d=='p':
                h=input('par ou ímpar?')
                j=randint(1,36)
                if h=='p' and j%2=0: 
                    print ('Ganhou!')
                    a=a+c
                    print('Você agora tem ${0}'.format(a)
                    b=True
                if h=='i' and j%2=1:
                    print ('Ganhou!')
                    a=a+c
                    print('Você agora tem ${0}'.format(a)
                    b=True
                if h=='p' and j%2= or h='i' and j%2=1:
                    print ('Perdeu!')
                    a=a-c
                    print('Você agora tem ${0}'.format(a)
                    b=True
                if h=='i' and j%2=0 or h='i' and j%2=1:
                    print ('Perdeu!')
                    a=a-c
                    print('Você agora tem ${0}'.format(a)
                    b=True