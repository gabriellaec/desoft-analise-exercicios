def filtra_positivos(lista):
    x = len(lista)
    if x == 0:
        return lista
    lista_positivos = []
    for numero in lista:
        if numero > 0:
            lista_positivos.append(numero)
    return lista_positivos


   