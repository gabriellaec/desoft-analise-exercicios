def calcula_fibonacci(n):
    lista=[0]*n
    lista[0]=1
    lista[1]=1
    if (n<=1):
        return n
    for i in range(0,len(lista)-2):
        lista[i+2]=lista[i+1]+lista[i]
    return lista






