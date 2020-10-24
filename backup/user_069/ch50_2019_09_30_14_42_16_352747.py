def numero_no_indice (lista):
    i = 0
    while i <= len(lista):
        if lista[i] == i:
            i += 1
            return i 