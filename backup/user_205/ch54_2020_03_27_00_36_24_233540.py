def calcula_fibonacci(n):
    lista=[0]*n
    lista[0]=1
    lista[1]=1
    for i in range(len(lista)-2):
        lista[i]=lista[i-1]+lista[i-2]
    return lista






