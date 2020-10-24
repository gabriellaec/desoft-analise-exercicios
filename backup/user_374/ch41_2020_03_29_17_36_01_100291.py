def zera_negativos(lista):
    #teste = True
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            lista [i] = 0
    i = i + 1
    return lista    
