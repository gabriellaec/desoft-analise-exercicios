def traduz(lista,dic):
    lista1=[]
    for i in lista:
        for i in dic.keys():
            lista1.append(dic[i])
    return lista1
    