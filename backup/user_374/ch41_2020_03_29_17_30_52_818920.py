def zera_negativos(lista):
    teste = True
    i = 0
    while teste:
        if i < len(lista):
            if lista[i] < 0:
                lista [i] = 0
                i = i + 1
            else:
                teste = False
        #else:
            #teste =  False
    return lista
