def zera_negativos(lista):
    lista_pos = []
    for e in lista:
        if e >= 0:
            lista_pos.append(e)
        elif e < 0:
            lista_pos.append(0)
    return lista_pos
    