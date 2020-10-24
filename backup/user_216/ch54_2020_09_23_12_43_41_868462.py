def calcula_fibonacci(n):
    lista = [1] * n
    i = 0
    while i < len(lista) - 2:
        lista[i+2] = lista[i+1] + lista[i]
        i += 1
    return lista