def interseccao_chaves(x,y):
    lista=[]
    for k in x.keys():
        if k in y.keys():
            if k not in lista:
                lista.append(k)
    return lista