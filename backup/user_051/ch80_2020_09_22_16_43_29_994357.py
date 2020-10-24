#list(dic_a.keys())
def interseccao_chaves(dic1,dic2):
    lista1=list(dic1.keys())
    lista2=list(dic2.keys())
    return list(set(lista1+lista2))
