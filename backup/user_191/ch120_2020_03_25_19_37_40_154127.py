import random
d=100
print(d)
a=int(input('Quantidade: '))
while a!=0:
    p=input('Aposta: ')
    r=random.randint(1,36)
    if p=='n':
        d=int(input('Numero de 1 a 36'))
        if d==r:
            d=d+35*a
        else:
            d=d-a
    elif p=='p':
        if r%2==0:
            d=d+a
        else:
            d=d-a
    else:
        if r%2!=0:
            d=d+a
        else:
            d=d-a
        
    
