def interseccao_chaves(dicio1, dicio2):
    lista_chaves = []
    #for i in range(0, len(d1)-1, 1):
    for i, l in dicio1.keys(),dicio2.keys():
        #if d1[i] == d2[i]:
        if i == l:
            lista_chaves.append(i)
    return lista
            