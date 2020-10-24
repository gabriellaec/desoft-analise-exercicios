def interseccao_chaves (dic1, dic2):
    lista=[]
    for i in range(len(dic1)):
        lista.append(dic1[i][1])
    for e in range(len(dic2)):
        lista.append(dic2[e][1])
    return lista