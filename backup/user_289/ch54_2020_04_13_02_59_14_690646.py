def calcula_fibonacci(n):
    lista = []*n
    lista[0] = 1
    lista[1] = 1
    i = 2
    while i <= n:
        lista[i] = lista[i-1]+ lista[i-2]
        lista.append(lista[i])
        i += 1
    return lista