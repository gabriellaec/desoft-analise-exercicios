def traduz(lista,dic):
    lista2=[]
    for i in lista:
        for v in dic:
            if i==v:
                lista2.append(dic[v])
    return lista2