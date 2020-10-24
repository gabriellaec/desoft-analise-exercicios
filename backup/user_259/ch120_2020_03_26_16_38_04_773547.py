import random
d=100
while d>0:
    print(d)
    a=int(input('Quanto voce apostar?: '))
    if a>0:
        p=input('Aposta(n,p): ')
        r=random.randint(0,36)
        if p=='n':
            f=int(input('Numero de 1 a 36: '))
            if f==r:
                d=d+35*a
            else:
                d=d-a
        else:
            p=input('Par ou ímpar? ')
            if p=='p':
                if r%2==0:
                    r='p'
                else:
                    r='i'
                if p==r:
                    d=d+a
                else:
                    d=d-a
            else:
                if r%2!=0:
                    r='i'
                else:
                    r='p'
                if p==r:
                    d=d+a
                else:
                    d=d-a
    else:
        break
print('Perdeu')   
    