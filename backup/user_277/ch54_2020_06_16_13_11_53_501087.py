def calcula_fibonacci(n):
    i = 0
    lista = [1, 1]
    while i < n:
        lista[i+2] = lista[i+1]+lista[i]
        i+=1
    return lista