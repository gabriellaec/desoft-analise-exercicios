def interseccao_chaves(dic1,dic2):
    lista1=[]
    for k in dic1:
        lista1.append(k)
    lista2=[]
    for k in dic2:
        lista2.append(k)
    lista3=[]
    for i in lista1:
        if lista2==i:
            lista3.append(i)
    return lista3