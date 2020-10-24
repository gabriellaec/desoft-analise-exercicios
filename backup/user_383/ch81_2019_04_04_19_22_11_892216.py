def interseccao_valores(dic1,dic2):
    lista_inter=[]
    for v in dic1.values():
        if v in dic2:
            lista_inter.append(v)
    return lista_inter
            
        