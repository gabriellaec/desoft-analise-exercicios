def interseccao_chaves (dic1, dic2):
    lista=[]
    chaves=dic1.keys()
    for i in chaves: 
        if i in dic2:
            lista.append(i)
    return lista 
            