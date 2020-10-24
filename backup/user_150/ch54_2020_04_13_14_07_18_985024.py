def calcula_fibonacci(n):
    lista = []*n
    if n == 0:
        return lista
    elif n == 1:
        lista[0] = 1
        return lista
    else:
        lista[0] = 1
        lista[1] = 1
        for numero in range(len(lista)-2):
            lista[numero+2] = lista[numero+1] + lista[numero]
        return lista