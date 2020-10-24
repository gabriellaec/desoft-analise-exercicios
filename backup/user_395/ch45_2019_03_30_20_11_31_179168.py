lista = [0]
def zera_negativos(lista):
    for e in lista:
        if e > 0:
            return lista
        else:
            return 0
print (zera_negativos([2, -7, 9, -4, -6, 0, 1]))