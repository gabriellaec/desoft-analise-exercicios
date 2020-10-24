def calcula_fibonacci():
    lista[0]=1
    lista[1]=1
    i=2
    while i<n:
        lista[i]=lista[i-1]+lista[i-2]
    return lista