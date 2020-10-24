def interseccao_valores(dicio1,dicio2):
    lista=[]
    for v in dicio1:
        for vv in dicio2:
            if v==vv:
                lista.append(v)
    return lista