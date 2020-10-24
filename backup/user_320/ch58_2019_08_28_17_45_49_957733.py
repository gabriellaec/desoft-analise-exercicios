def calcula_fibonacci(n):
    cont = 1
    if n == 1:
        return [1]
    lista = [1, 1]

    while cont < n - 1:
        proximo = lista[cont - 1] + lista[cont]
        lista.append(proximo)
        cont += 1
    return lista
