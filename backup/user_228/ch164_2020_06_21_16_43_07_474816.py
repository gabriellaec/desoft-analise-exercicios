def traduz(lista,dic):
    lista2=[]
    for i in lista:
        if i in dic:
            lista2.append(dic.values())
    return lista2