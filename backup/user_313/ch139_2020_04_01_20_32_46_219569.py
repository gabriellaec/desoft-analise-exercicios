def arcotangente(x,n):

    arctan = 0
    contador = 3

    while contador < n:
        arctan = x - ((x**contador)/contador)
        contador = contador + 2

    return arctan