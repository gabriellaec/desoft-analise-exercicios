def arcotangente(x,n):
    i = 1
    lista = []
    while len(lista) <= n:
        lista.append((x**i)/i)
        i = i + 2
    return sum(lista)