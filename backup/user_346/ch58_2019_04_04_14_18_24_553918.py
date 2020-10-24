def calcula_fibonacci(n):
    if n ==1:
        return [1]
    
    lista=[]
    lista.append(1)
    lista.append(1)
    i=2
    while i<n:
        lista.append(lista[i-1]+lista[i-2])
        i+=1
    return lista