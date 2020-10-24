def calcula_fibonacci(r):
    lista = [0, 1]
    for i in range(2, r):
        lista.append(lista[max(i - 1, 0)] + lista[max(i - 2, 0)])
    return lista