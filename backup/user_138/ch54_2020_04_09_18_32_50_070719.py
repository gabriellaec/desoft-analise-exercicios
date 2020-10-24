def calcula_fibonacci(n):
    i=0
    lista[0]=1
    lista[1]=1
    while i<n:
        lista[i]=lista[i-1]+lista[i-2]
        i+=1
    return lista