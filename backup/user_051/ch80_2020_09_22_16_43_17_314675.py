#list(dic_a.keys())
def interseccao_chaves(dic1,dic2):
    lista1=list(dic1.keys())
    lista2=list(dic2.keys())
    return list(set(lista1+lista2))
dic1={'e':1,'r':2}
dic2={'e':3,'r':4}
q=interseccao_chaves(dic1,dic2)
print(q)