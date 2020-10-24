def interseccao_chaves(dic1,dic2):
    lista = []
    for e in dic1:
         if e in dic2:
            lista.append(e)
    return lista