def numero_no_indice(lista):
    lista = []
    indice_numero = []
    x = 0
    while x < len(lista):
        if lista [x] == x:
            indice_numero.append(lista[x])
        x += 1
    return indice_numero 