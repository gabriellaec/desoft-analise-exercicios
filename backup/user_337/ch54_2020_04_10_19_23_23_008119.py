def calcula_fibonacci(n):
    lista = []
    lista.append(1)
    lista.append(1)
    while len(lista) < n:
        x = lista[n-1] + lista[n-2]
        lista.append(x)
    return lista