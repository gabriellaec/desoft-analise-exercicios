def interseccao_valores(d1, d2):
    lista=[]
    for k1,v1 in d1.items():
        for k2,v2 in d2.items():
            if v1==v2:
                lista.append(v1)
    return lista