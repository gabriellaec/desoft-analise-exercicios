def interseccao_valores(x,y):
    lista=[]
    dici={}
    for va in x.values():
        if va in y.values():
            dici[va]=[]
    for k in dici.keys():
        lista.append(k)

    return lista