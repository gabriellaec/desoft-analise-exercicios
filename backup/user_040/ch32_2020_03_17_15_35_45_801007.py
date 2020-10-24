def lista_primos(n):
    if n!=0:
        lista_primos[0]=2
    elif n!=0 and n>=2:
        lista_primos[0]=2
        lista_primos[1]=3
    
    while 1<x<n:
        y=3
        if lista[x]%2!=0 and lista[x]%y!=0:
            lista[x]=lista[x-1]+2
