
def interseccao_valores(dic1,dic2):
    lista_inter=[]
    valores=dic2.values()
    for v in dic1.values():
        if v in valores:
            lista_inter.append(v)
    return lista_inter