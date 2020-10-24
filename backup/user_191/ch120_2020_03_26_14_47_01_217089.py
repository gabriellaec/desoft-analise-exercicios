import random
d=100
print(d)
while d>0:
    a=int(input('Quantidade: '))
    if a>0:
        p=input('Aposta(n,p): ')
        r=random.randint(0,36)
        if p=='n':
            f=int(input('Numero de 1 a 36: '))
            if d==r:
                d=d+35*a
                print(d)
            else:
                d=d-a
                print(d)
        else:
            p=input('Par ou ímpar? ')
            if p=='p':
                if r%2==0:
                    r='p'
                else:
                    r='i'
                if p==r:
                    d=d+a
                    print(d)
                else:
                    d=d-a
                    print(d)
            else:
                if r%2!=0:
                    r='i'
                else:
                    r='p'
                if p==r:
                    d=d+a
                    print(d)
                else:
                    d=d-a
                    print(d)
    else:
        break
print('Perdeu')

