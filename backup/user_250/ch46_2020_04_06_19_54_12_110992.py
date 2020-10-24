def numero_no_indice(lista):
    lista_x = []
    for i,e in enumerate(lista):
        if e == i:
            lista_x.append (e)
            return lista_x