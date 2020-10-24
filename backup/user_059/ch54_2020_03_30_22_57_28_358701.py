def calcula_fibonacci(x):
    lista = [0]*x
    lista[0] = 1
    lista[1] = 1
    i=2
    while i<x:
        lista[i+1] = lista[i]+lista[i-1]    
        i+=1
    return lista
