def calcula_fibonacci(n):
    
    lista = [0]*n
    if n == 0:
        return lista
    lista[0] = 1
    lista[1] = 1

    contador = 2

    while contador <= n-1:

        lista[contador]=lista[contador-1]+lista[contador-2]

        contador = contador + 1

    return lista