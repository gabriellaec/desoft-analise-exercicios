def interseccao_chaves(dic1,dic2):
    lista=[]
    for k in dic1:
        if dic1[k]==dic2[k]:
            lista.append(k)
    return lista
        