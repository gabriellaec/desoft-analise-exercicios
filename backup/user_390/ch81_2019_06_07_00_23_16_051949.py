def interseccao_valores(dic1,dic2):
    lista1=[]
    for k,v in dic1.items():
        lista1.append(v)
    lista2=[]
    for k,v in dic2.items():
        lista2.append(v)
    lista3=[]
    c=0
    while c<len(lista1):
        while i<len(lista2):
            if lista1[c]==lista2[i]:
                if lista1[c] not in lista3:
                    lista3.append(lista1[c])
            else:
                i+=1
        c+=1
        i=0
    return lista3