def lista_primos(n):
    a=2
    i=3
    x=n
    lista=[0]*n
    while x>0:
        lista[n-x]=a
        a+=1
        if a%2==0 or (a%i==0 and a>i):
            while a%2==0 or (a%i==0 and a>i):
                i=3
                a+=1
                while a%i!=0 and a>i:
                    i+=2
            x-=1
        else:
            x-=1
    return lista