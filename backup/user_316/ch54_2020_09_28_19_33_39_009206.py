def calcula_fibonacci(n):
    lista = [1, 1]
    for i in range(1, n):
        lista.append(lista[max(i - 1, 0)] + lista[max(i - 2, 0)])
    return lista