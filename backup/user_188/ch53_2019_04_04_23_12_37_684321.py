def inverte_lista(lista):
    invertida = []
    contador = len(lista) -1
    while contador >= 0:
        invertida.append(lista[contador])
        contador -= 1
    return invertida