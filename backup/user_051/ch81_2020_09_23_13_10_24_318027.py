#list(dic_a.keys())
def interseccao_chaves(dic1,dic2):
    lista1=list(dic1.values())
    lista2=list(dic2.values())
    lista3=[]
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3