def  interseccao_chaves (dic1,dic2):
    lista=[]
    for a in dic1.keys():
        if a in dic2.keys():
            lista.append(a)
    return lista