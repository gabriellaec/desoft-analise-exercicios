def traduz(lista,dic):
    lista2=[]
    for i in lista:
        for k in dic:
            if i==k:
                lista2.append(dic[k])
    return lista2