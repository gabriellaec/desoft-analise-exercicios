def calcula_fibonacci(x):
    lista=[1,1]
    i=2
    while i<x:
        lista.append(lista[i-2]+lista[i-1])
        i+=1
    return lista