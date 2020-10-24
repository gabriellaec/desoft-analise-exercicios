def calcula_fibonacci(n):
    if n ==1:
        lista=[1]
    else:
        lista=[1,1]
        i=2
        while i<n:
        fibonacci = lista[i-1]+lista[i-2]
        lista.append(fibonacci)
        i+=1
    return lista
        
    