def calcula_fibonacci(n):
    i = 0
    lista = [1, 1]
    k=0
    while k < n:
        k = lista[i+1]+lista[i]
        lista.append(k)
        i+=1
    return lista