def interseccao_chaves(dicio1,dicio2):
    lista=[]
    for k in dicio1:
        for x in dicio2:
            if k==x:
                lista.append(k)
    return lista