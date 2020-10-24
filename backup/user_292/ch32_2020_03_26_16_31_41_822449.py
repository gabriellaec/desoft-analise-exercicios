def lista_primos(n):
    e=2
    d=3
    lista=[0]*n
    x=0
    while n>x:
        lista[x]=e
        e+=1
        x+=1
        if e%2==0:
            while e%2==0 or e%d==0:
                d=3
                e+=1
                while e%d!=0:
                    d+=2
    return lista