def calcula_fibonacci(n):
    lista = [1]*2
    for i in range(2, n):
        lista.append(lista[i-1] + lista[i-2])
    return lista