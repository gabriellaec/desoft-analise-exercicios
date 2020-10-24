def interseccao_valores(dic1,dic2):
    lista1=[]
    for k,v in dic1.items():
        lista1.append(v)
    lista2=[]
    for k,v in dic2.items():
        lista2.append(v)
    lista3=[]
    for i in range(0,len(lista1)):
        if lista1[i]==lista2[i]:
            lista3.append(lista1[i])
    return lista3