def calcula_fibonacci(x):
    lista=[]
    i=2
    if x>=1:
        lista.append(1)
    if x>=2:
        lista.append(1)    
    while i<x:
        lista.append(lista[i-2]+lista[i-1])
        i+=1
    return lista