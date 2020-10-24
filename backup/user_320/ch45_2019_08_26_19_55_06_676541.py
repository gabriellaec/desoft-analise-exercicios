def zera_negativos(lista):
    for numero in lista:
        if numero < 0:
            numero = 0
    return lista       