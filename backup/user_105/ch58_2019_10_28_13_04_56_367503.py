def calcula_fibonacci(x):
    lista = [0]*(x)
    i = 0
    lista[0] = 1
    if x>i:
    	lista[1] = 1    
    while i<x-1:
        lista[i+1]=lista[i]+lista[i-1]
        i+=1
    return lista
    