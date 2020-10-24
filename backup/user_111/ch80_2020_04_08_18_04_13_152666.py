def interseccao_chaves(dic1,dic2):
    lista=[]
    for i in dic1:
        for j in dic2:
            if i==j:
                lista.append(i)
    return lista