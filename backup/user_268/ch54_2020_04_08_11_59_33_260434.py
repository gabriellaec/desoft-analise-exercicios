def calcula_fibonacci(n):
    lista = [0] * n
    lista[0] = 1
    for i in range(0, n):
        lista[i + 1] = lista[i] + lista[i - 1]
    return lista
        