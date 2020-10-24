def interseccao_chaves(dic1,dic2):    
    lista=[]
    lista.append(dic1.keys())
    lista1=[]
    lista1.append(dic2.keys())
    lista2=[]
    for i in lista:
        for j in lista1:
            if i==j:
                lista2.append(j)
    return lista2

        