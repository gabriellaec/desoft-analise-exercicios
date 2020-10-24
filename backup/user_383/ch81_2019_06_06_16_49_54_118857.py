
def interseccao_valores(dic1,dic2):
    lista_vazia=[]
    for v in dic1.values():
        if v in dic2:
            lista_vazia.append(v)
    return lista_vazia