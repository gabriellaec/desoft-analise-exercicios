def interseccao_chaves(dici1,dici2):
    lista=[]
    for i in dici1:
        if i in dici2:
            lista.append(i)
    return lista