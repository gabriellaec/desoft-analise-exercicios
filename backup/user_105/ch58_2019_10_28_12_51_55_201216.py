def calcula_fibonacci(x):
    lista = [0]*x
    i = 2
    lista[0] = 1
    lista[1] = 1
    while i<x:
        lista[i]=lista[i-1]+lista[i-2]
        i+=1
    return lista
    