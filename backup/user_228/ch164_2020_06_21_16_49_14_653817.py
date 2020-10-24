def traduz(lista,dic):
    lista2=[]
    for i in lista:
        for rola in dic:
            if i==rola:
                lista2.append(dic[rola])
    return lista2