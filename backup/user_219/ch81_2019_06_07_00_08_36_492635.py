def interseccao_valores(dic1,dic2):
    lista=[]
    d1=[]
    d2=[]
    for chave,valor in dic1.items():
        d1.append(valor)
    for chave,valor in dic2.items():
        d2.append(valor)
    for i in d1:
        if i in d2:
            lista.append(i)
    return lista