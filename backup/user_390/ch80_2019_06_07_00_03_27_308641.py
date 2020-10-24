def interseccao_chaves(dic1,dic2):
    lista1=[]
    for k in dic1:
        lista1.append(k)
    lista2=[]
    for k in dic2:
        lista2.append(k)
    lista3=[]
    s=0
    for i in range(0,len(lista1)):
        if lista1[i]==lista2[i]:
            lista3.append(lista1[i])
    return lista3
        