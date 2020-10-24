import random
d=100
while d>0:
    print(d)
    a=int(input('Quantidade: '))
    p=input('Aposta(n,p,i): ')
    r=random.randint(0,36)
    if a>0:
        if p=='n':
            f=int(input('Numero de 1 a 36: '))
            if d==r:
                d=d+35*a
                print(d)
                a=int(input('Quantidade: '))
            else:
                d=d-a
                print(d)
                a=int(input('Quantidade: '))
        elif p=='p':
            if r%2==0:
                d=d+a
                print(d)
                a=int(input('Quantidade: '))
            else:
                d=d-a
                print(d)
                a=int(input('Quantidade: '))
        else:
            if r%2!=0:
                d=d+a
                print(d)
                a=int(input('Quantidade: '))
            else:
                d=d-a
                print(d)
                a=int(input('Quantidade: '))
    else:
        break