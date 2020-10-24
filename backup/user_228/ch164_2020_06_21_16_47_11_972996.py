def traduz(lista,dic):
    lista2=[]
    for i in lista:
        for k,v in dic:
            if i==k:
                lista2.append(v)
    return lista2