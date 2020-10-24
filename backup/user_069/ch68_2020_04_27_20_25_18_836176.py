def separa_trios (lista):
    if len(lista) <= 3:
        return lista
    else:
        t = lista[0 : len(lista) : 3]
        return t