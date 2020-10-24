def calcula_fibonacci(n):
    lista=[0]*n
    lista[0]=1
    lista[1]=1
    for i in range(len(lista)-3):
        lista[i+2]=lista[i+1]+lista[i]
    return lista