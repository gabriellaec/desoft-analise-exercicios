def interseccao_chaves(dic1,dic2):    
    lista=dic1.keys()
    lista1=dic2.keys()
    lista2=[]
    for i in lista:
        for j in lista1:
            if i==j:
                lista2.append(j)
    return lista2

        