def arcotangente(x,n):
    i = 1
    u = 1
    lista = []
    while len(lista) <= n:
        lista.append((u*(x**i)/i))
        i = i + 2
        u = u*(-1)
    return sum(lista)