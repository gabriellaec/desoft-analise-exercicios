def interseccao_valores(dic1,dic2):
    lista=[]
    valores=dic1.values()
    for k,v in dic2.items():
        if v in valores:
            lista.append(v)
    return lista