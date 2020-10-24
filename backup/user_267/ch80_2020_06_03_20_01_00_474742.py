def interseccao_chaves(d1, d2):
    lista = []
    #for i in range(0, len(d1)-1, 1):
    for i, l in d1.keys(),d2.keys():
        #if d1[i] == d2[i]:
        if i == l:
            lista.append(i)
    return lista
            