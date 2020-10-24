def interseccao_chaves(dicio1, dicio2):
    lista_chaves = []
    for i in dicio1.keys() and l in dicio2.keys():
        if i == l:
            lista_chaves.append(i)
    return lista_chaves
            