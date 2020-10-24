def calcula_fibonacci(n):
    lista = [0, 1]
    for i in range(2, n+1):
        lista.append(lista[max(i - 1, 0)] + lista[max(i - 2, 0)])
    lista.pop(0)
    return lista