def interseccao_valores(dic1,dic2):
    lista = []
    for e in dic1.values():
         for i in dic2.values():
                if e == i:
                    lista.append(e)                 
    return lista