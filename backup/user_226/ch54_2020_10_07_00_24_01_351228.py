def calcula_fibonacci(n):
    lista = []
    if n > 0:
        lista.append(1)
    if n > 1:
        lista.append(1)
    if n > 2:
        i = 2
        while i < n:
            lista.append(lista[i - 1] + lista[i - 2])
            i += 1
    return lista