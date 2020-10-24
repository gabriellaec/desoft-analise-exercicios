def zera_negativos(lista):
    contador = 0
    nova_lista = lista
    while contador < len(lista):
        if lista[contador] < 0:
            nova_lista[contador] = 0
        contador += 1
    return nova_lista