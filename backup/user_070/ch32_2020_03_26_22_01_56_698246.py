def lista_primos(n):
    a=2
    i=3
    x=0
    lista=[0]*n
    while x<n:
        lista[x]=a
        a+=1
        x+=1
        while a%2==0 or (a%i==0 and a>i):
            i=3
            a+=1
            while a%i!=0 and a>i:
                i+=2
    return lista