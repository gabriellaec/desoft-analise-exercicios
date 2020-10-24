def interseccao_chaves(dic1,dic2):
    lista=[]
    for k,v in dic1.items():
        if k in dic2:
            lista.append(k)
    return lista