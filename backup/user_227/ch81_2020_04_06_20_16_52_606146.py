def interseccao_valores(dic1, dic2):
    lista_valores=[]
    for valor in dic1.values():
        if valor in dic2.values():
            lista_valores.append(valor)
    return lista_valores