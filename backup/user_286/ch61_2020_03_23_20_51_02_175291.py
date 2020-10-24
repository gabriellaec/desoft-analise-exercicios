def filtra_positivos(lista):
    lista_positivos = []
    for numero in lista:
        if numero > 0:
            lista_positivos.append(numero)

    return lista_positivos
