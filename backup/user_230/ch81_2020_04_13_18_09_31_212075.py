def interseccao_valores(dic1,dic2):
    lista=[]
    for i in dic1.items():
        for k in dic2.items():
            if dic1[i]==dic2[k]:
                lista.append(dic1[i])
    return lista