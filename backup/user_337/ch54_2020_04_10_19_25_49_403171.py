def calcula_fibonacci(n):
    lista = []
    lista.append(1)
    if n == 1:
        return lista
    lista.append(1)
    if n == 2:
        return lista
    while len(lista) < n:
        x = lista[n-1] + lista[n-2]
        lista.append(x)
    return lista