def interseccao_chaves(dic1, dic2):
    lista=[]
    for i in dic1.items():
        for k in dic2.items():
            if i==k:
                lista.append(i)
    return lista