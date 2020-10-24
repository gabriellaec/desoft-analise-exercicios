def numero_no_indice(lista):
    delimitador = len(lista)
    i = 0
    lista2 = []
    while delimitador < len(lista):
        if lista[i] == i:
            lista2.append(i)
        