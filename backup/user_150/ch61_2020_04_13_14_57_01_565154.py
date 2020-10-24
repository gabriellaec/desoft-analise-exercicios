def filtra_positivos(lista_numeros):
    lista_positivos = []
    for numero in lista_numeros:
        if numero > 0:
            lista_positivos.append(numero)
    return lista_positivos