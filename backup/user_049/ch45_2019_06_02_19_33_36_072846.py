def zera_negativos(lista):
    i = 0
    while i < len(zera_negativos):
        if zera_negativos[i] < 0:
            zera_negativos[i] = 0
        i += 1
    return zera_negativos
print(zera_negativos)