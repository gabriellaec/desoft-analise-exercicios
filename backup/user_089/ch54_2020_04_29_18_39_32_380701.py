def calcula_fibonacci(n):
    lista = [1,1]
    i = 0
    while i < n:
        lista.append(lista[i]+lista[i+1])
        i += 1
    return lista
   
        