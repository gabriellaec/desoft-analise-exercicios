def calcula_fibonacci(n):
    lista=[0]*n
    lista[1]=1
    lista[2]=1
    for i in range(0,len(lista)-2):
        lista[i+2]=lista[i+1]+lista[i]
    return lista






