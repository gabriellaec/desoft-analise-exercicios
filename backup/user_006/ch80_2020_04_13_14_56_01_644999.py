def interseccao_chaves(d1, d2):
    lista=[]
    for i in d1:
        for g in d2:
            if i==g:
                lista.append(i)
    return lista