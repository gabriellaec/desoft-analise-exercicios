def calcula_fibonacci(n):
    lista = [0]*n
    lista[0] = 1
    lista[1] = 1
    if n >= 3:
        lista[0] = 1
        lista[1] = 1
        for i in range(1, n):
            lista[i + 1] = lista[i] + lista[i - 1]
            return lista
    elif n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]