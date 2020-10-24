def calcula_fibonacci(n):
    if (n<=1):
        return [1]
    lista=[0]*n
    lista[0]=1
    lista[1]=1
    i=0
    while (i<n-2):
        lista[i+2]=lista[i+1]+lista[i]
        i+=1
    return lista






