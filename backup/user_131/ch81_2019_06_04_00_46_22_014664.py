def interseccao_valores(dic1,dic2):
    lista = []
    for e in dic1.values():
         if e in dic2:
            lista.append(e)
    return lista