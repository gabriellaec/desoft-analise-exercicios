def filtra_positivos(lista):
    positivos = []
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            positivos.append(lista[i])
            i += 1
        else:
            i += 1
    return positivos

teste = [-5, -2, -23, 0, 5, 9, 500, -6, 98, 0]
print(filtra_positivos(teste))