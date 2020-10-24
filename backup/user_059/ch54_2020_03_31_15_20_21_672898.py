def calcula_fibonacci(x):
    lista = [0]*x
    lista[0 and 1] = 1
    i=2
    while i<x:
        lista[i] = lista[i-1]+lista[i-2]    
        i+=1
    return lista
