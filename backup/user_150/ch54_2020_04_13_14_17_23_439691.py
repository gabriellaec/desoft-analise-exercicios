def calcula_fibonacci(n):
    lista = [0]*n
    lista[0] = 1
    if n == 1:
        return lista
    elif n == 2:
        lista[1] = 1
        return lista
    lista[1] = 1
    for numero in range(n-2):
        lista[numero+2] = lista[numero+1] + lista[numero]
    return lista