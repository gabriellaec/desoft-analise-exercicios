def calcula_euler(x, n):
    lista = []
    i = 0
    while i < n:
        lista.append(x ** i)
        i += 1
    return sum(lista)