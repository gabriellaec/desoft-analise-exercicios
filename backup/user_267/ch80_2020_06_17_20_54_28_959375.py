def interseccao_chaves(dicio1, dicio2):
    lista_chaves = []
    for i in dicio1.keys():
        if i in dicio2.keys():
            lista_chaves.append(i)
    return lista_chaves
            