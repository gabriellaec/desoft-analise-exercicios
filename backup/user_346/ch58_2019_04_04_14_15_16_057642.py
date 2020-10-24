def calcula_fibonacci(n):
    lista=[]
    lista.append(1)
    lista.append(1)
    i=2
    while i<n:
        lista[i]=lista[i-1]+lista[i-2]
        i+=1
    return lista