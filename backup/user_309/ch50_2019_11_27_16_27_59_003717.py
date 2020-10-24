def numero_no_indice(lista):    
    i = 0
    lista_nova = []
    while i != len(lista):
        if lista[i] == i:
            lista_nova.append(i)
        i = i + 1
    return lista_nova