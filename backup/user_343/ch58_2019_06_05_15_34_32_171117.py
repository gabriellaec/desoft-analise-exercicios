def calcula_fibonacci(n):
    lista=[1,1]
    i=2
    while i <= n:
        lista.append(lista[n-1]-lista[n-2])
        i+=1
        
    return lista    