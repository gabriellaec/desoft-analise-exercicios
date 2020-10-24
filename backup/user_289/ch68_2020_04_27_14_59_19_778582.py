def separa_trios(lista_nomes):
    e = 0
    lista_trios = []
    while e < len(lista_nomes):
        lista_trios.append(lista_nomes[e:e+3])
        e += 3
    return lista_trios        