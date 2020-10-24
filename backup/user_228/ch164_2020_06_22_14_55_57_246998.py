def traduz(lista,dic):
    lista2=[]
    for i in lista:
        for v in dic.keys():
            if i==v:
                lista2.append(dic.values())
    return lista2