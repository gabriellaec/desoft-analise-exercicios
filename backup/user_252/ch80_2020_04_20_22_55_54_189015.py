def interseccao_chaves(d1, d2):
    lista=[]
    for k in d1.keys():
        l=k
        for j in d2.keys():
            m=j
            if l==m:
                lista.append(l)
                m=len(d2)
    return lista
    