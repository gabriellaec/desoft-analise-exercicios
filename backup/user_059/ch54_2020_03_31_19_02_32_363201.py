def calcula_fibonacci(x):
    lista = []
    lista.append(1)
    lista.append(1)
    i=2
       while i<=x:
            lista.append(lista[i-1]+lista[i-2])    
            i+=1
    return lista
