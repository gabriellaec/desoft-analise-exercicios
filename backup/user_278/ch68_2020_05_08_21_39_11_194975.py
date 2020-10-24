def separa_trios (lista1):
    lista_trios = []
    i = 0
    while i <= len(lista1):
        t = lista1[i:(i+3)]
        lista_trios.append(t)
        i+=3
    return lista_trios